from django.shortcuts import render, HttpResponse
from django.views.generic import View, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import auth
from .models import *
from apps.users.models import Comment
from django.http import JsonResponse
from django.forms.models import model_to_dict
import logging
import json
import random
logger = logging.getLogger('anime')
# Create your views here.


def index(request):
    background_num = random.randint(1, 2)
    background = 'wallpaper' + f'{background_num}'
    # 每天播放的番剧
    Mon = AnimeList.objects.filter(anime_time_week_id__lt=8)
    Tues = AnimeList.objects.filter(anime_time_week_id__lt=13).filter(anime_time_week_id__gt=7)
    Wed = AnimeList.objects.filter(anime_time_week_id__lt=18).filter(anime_time_week_id__gt=12)
    Thurs = AnimeList.objects.filter(anime_time_week_id__lt=19).filter(anime_time_week_id__gt=17)
    Fri = AnimeList.objects.filter(anime_time_week_id__lt=26).filter(anime_time_week_id__gt=20)
    Sat = AnimeList.objects.filter(anime_time_week_id__lt=32).filter(anime_time_week_id__gt=25)
    Sun = AnimeList.objects.filter(anime_time_week_id__lt=41).filter(anime_time_week_id__gt=32)

    kwgs = {
        background: background,
        'Mon': Mon,
        'Tues': Tues,
        'Wed': Wed,
        'Thurs': Thurs,
        'Fri': Fri,
        'Sat': Sat,
        'Sun': Sun,
    }
    return render(request, 'index.html', kwgs)


# 点击对应的番剧展示的详情页面
class AnimeDetail(View):

    def get(self, request, id):
        anime = AnimeList.objects.get(id=id)
        # if_collection = anime.animecollection_set
        anime.n_point += 1
        anime.save()
        release_date = ReleaseDate.objects.get(animelist=anime)
        staff = Staff.objects.get(animelist=anime)
        supervision = Supervision.objects.get(animelist=anime)
        musician = Musician.objects.get(animelist=anime)
        comment = Comment.objects.filter(anime=anime).order_by('-comment_time')
        comment_num = comment.count()
        anime_point = anime.n_point
        paginator = Paginator(comment, 4)
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        all_pages = range(contacts.paginator.num_pages)
        kwgs = {
            'anime': anime,
            'comment': comment,
            'release_date': release_date,
            'staff': staff,
            'supervision': supervision,
            'musician': musician,
            'anime_point': anime_point,
            'commet_num': comment_num,
            'contacts': contacts,
            'all_pages': all_pages,
        }
        return render(request, 'anime_detail.html', kwgs)

    def post(self, request, id):
        # 获取ajax传过来的评论内容，写入数据库并保存
        if request.user.is_authenticated:
            try:
                comment = request.POST.get('comment')
                anime = AnimeList.objects.get(id=id)
                this_comment = Comment.objects.filter(anime=anime)
                new_comment = Comment.objects.create(anime=anime, user=request.user, content=comment)
                new_comment.save()
                msg = model_to_dict(new_comment)
                comment_num = this_comment.count() + 1
                msg['comment_num'] = comment_num
                code = 200
            except Exception as ex:
                logger.error(ex)
                msg = '提交失败'
                code = 500
        else:
            code = 401
            msg = '当前尚未登录，登录后才可评论'
        result = {'code': code, 'msg': msg}
        return JsonResponse(result)

