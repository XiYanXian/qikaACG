from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.views.generic import View
from django.forms.models import model_to_dict
from apps.tags.models import Tags
import random
import datetime
import time
import os
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from qika.settings import MEDIA_ROOT, MEDIA_URL
from django.core.mail import send_mail, EmailMultiAlternatives
from apps.anime.models import AnimeList
from apps.users.models import AnimeCollection, CommentLike, Comment, UserInfo
from qika.settings import EMAIL_FROM
from io import BytesIO
from libs import captcha
import base64
import logging
logger = logging.getLogger('apis')


# 获取邮箱验证码
def get_email_captcha(request):
    ret = {'code': 200, 'msg': '验证码发送成功！'}
    try:
        email = request.GET.get('email')
        if email is None:
            raise ValueError('邮箱不能为空！')
        email_captcha = ''.join(random.choices('0123456789', k=6))
        cache.set(email, email_captcha, 1800)
        email_title = '【qikaACG】验证码'
        email_body = f'<p>感谢使用qikaACG，您本次的验证码为：<b style="color: red">{email_captcha}</b></p>'
        msg = EmailMultiAlternatives(email_title, email_body, EMAIL_FROM, [email])
        msg.content_subtype = "html"
        msg.send()
    except Exception as ex:
        logger.error(ex)
        ret = {'code': 400, 'msg': '验证码发送失败!'}
    return JsonResponse(ret)


# 获取登录验证码
def get_captcha(request):
    # 在内存开辟一个空间用来存放临时生成的图片
    f = BytesIO()
    # 调用check_code生成照片和验证码
    img, code = captcha.create_validate_code()
    # 将验证码存放在服务器的session中，用于校验
    request.session['captcha_code'] = code
    # 生成的图片放置于开辟的内存之中
    img.save(f, 'PNG')
    # 将内存的数据读取出来，转化为base64格式
    ret_type = "data:image/jpg;base64,".encode()
    ret = ret_type + base64.encodebytes(f.getvalue())
    del f
    return HttpResponse(ret)


# 校验登录验证码
def check_captcha(request):
    ret = {"code": 400, "msg": "验证码错误！"}
    post_captcha_code = request.GET.get('captcha_code', '')
    session_captcha_code = request.session.get('captcha_code', '')
    if post_captcha_code and post_captcha_code.lower() == session_captcha_code.lower():
        ret = {"code": 200, "msg": "验证码正确"}
    return JsonResponse(ret)


# def get_tag(request, tag):
#     ret = {'code': 400, 'msg': '当前分类没有番剧'}
#     tag_animes = Tags.objects.get(tag_name=tag)
#     if tag_animes:
#         ret = {'code': 200, "msg": '该分类下的番剧如下', 'tag_animes': tag_animes}
#     return JsonResponse(ret)
class JudgeCollection(View):
    """判断用户是否点击过收藏"""
    def get(self, request, id):
        anime = AnimeList.objects.get(id=id)
        if request.user.is_authenticated:
            judge = AnimeCollection.objects.filter(user=request.user, anime=anime)
            judge = True
        else:
            judge = None
        ret_info = {'code': 200, 'msg': judge}
        return JsonResponse(ret_info)


class AnimeCollectionView(LoginRequiredMixin, View):
    """
    当用户点击该番剧时，首先获取该番剧，并检查是否被收藏过
    修改当前题目的收藏状态
    """
    def get(self, request, id):
        anime = AnimeList.objects.get(id=id)
        result = AnimeCollection.objects.get_or_create(user=request.user, anime=anime)
        # result是一个元组，第一参数是instance, 第二个参数是true和false
        # True表示新创建,False表示老数据
        anime_collection = result[0]
        if not result[1]:
            if anime_collection.status:
                anime_collection.status = False
                anime.n_collection -= 1
            else:
                anime_collection.status = True
                anime.n_collection += 1
        else:
            anime.n_collection += 1
        anime_collection.save()
        anime.save()
        msg = model_to_dict(anime_collection)
        msg['n_collection'] = anime.n_collection
        ret_info = {"code": 200, "msg": msg}
        return JsonResponse(ret_info)


class CommentLikeView(LoginRequiredMixin, View):
    """
    点击该评论时，先获取评论的内容，并检查是否被人点赞过以及点赞的数量
    """
    def get(self, request, id):
        comment = Comment.objects.get(id=id)
        result = CommentLike.objects.get_or_create(user=request.user, comment=comment)
        comment_like = result[0]
        if not result[1]:
            if comment_like.status:
                comment_like.status = False
                comment.n_like -= 1
            else:
                comment_like.status = True
                comment.n_like += 1
        comment.save()
        comment_like.save()
        msg = model_to_dict(comment_like)
        msg['like'] = comment.n_like
        ret_info = {'code': 200, 'msg': msg}
        return JsonResponse(ret_info)


class RankComment(View):
    """
    按评论时间排序功能
    """
    def get(self, request, id, rank):
        anime = AnimeList.objects.get(id=id)
        # 按时间升序
        if rank == 'time_up':
            all_comment = Comment.objects.filter(anime=anime).order_by('comment_time')
        # 按时间降序
        if rank == 'time_down':
            all_comment = Comment.objects.filter(anime=anime).order_by('-comment_time')
        if rank == 'like_most':
            all_comment = Comment.objects.filter(anime=anime).order_by('-n_like')
        else:
            all_comment = '当前没有评论'
        ret = {'code': 200, 'msg': all_comment}
        return JsonResponse(ret)


class SearchAnime(View):
    """番剧查找的接口"""
    def get(self, request):
        tags = Tags.objects.all()
        anime_name = request.GET.get('anime_name')
        anime = AnimeList.objects.filter(anime_name__contains=anime_name)
        if anime:
            msg = '以下是查询到的动漫'
        else:
            msg = '没有符合条件的动漫'
        paginator = Paginator(anime, 4)
        page = request.GET.get('page')

        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        all_pages = range(contacts.paginator.num_pages)
        kwgs = {
            'anime_name': anime_name,
            'msg': msg,
            'tags': tags,
            'contacts': contacts,
            'all_pages': all_pages,
        }
        return render(request, 'search.html', kwgs)


class ChangeAvatar(LoginRequiredMixin, View):
    def post(self, request):
        today =datetime.date.today().strftime("%Y%m%d")
        # 图片的data-img格式=>data:image/jpg;base64,xxxx
        img_src_str = request.POST.get("image")
        img_str = img_src_str.split(',')[1]
        # 取出格式:jpg/png...
        img_type = img_src_str.split(';')[0].split('/')[1]
        # 取出数据:转化为bytes格式
        img_data = base64.b64decode(img_str)
        # 相对上传路径: 头像上传的相对路径
        avatar_path = os.path.join("avatar", today)
        # 绝对上传路径：头像上传的绝对路径
        avatar_path_full = os.path.join(MEDIA_ROOT, avatar_path)
        if not os.path.exists(avatar_path_full):
            os.mkdir(avatar_path_full)
        filename = str(time.time()) + "." + img_type
        # 绝对文件路径，用于保存图片
        filename_full = os.path.join(avatar_path_full, filename)
        # 相对MEDIA_URL路径，用于展示数据
        img_url = f"{MEDIA_URL}{avatar_path}/{filename}"
        try:
            with open(filename_full, 'wb') as fp:
                fp.write(img_data)
            ret = {
                "result": "ok",
                "file": img_url
            }
        except Exception as ex:
            ret = {
                "result": "error",
                "file": "upload fail"
            }

        request.user.icon = os.path.join(avatar_path, filename)
        request.user.save()
        return JsonResponse(ret)