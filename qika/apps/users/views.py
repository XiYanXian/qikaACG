from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.shortcuts import render
from .models import UserInfo, Comment, AnimeCollection
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import auth
import logging
logger = logging.getLogger('user')


class UserCenter(LoginRequiredMixin, View):

    def get(self, request, id):
        user = UserInfo.objects.get(id=id)
        user = model_to_dict(user)
        kwgs = {
            'user': user,
        }
        return render(request, 'user_info.html', kwgs)

    def post(self, request, id):
        user = UserInfo.objects.get(id=id)
        try:
            if request.POST.get('intro'):
                intro = request.POST.get('intro')
                user.intro = intro

            if request.POST.get('sex'):
                sex = request.POST.get('sex')
                user.sex = sex
            user.save()
            user = UserInfo.objects.get(id=id)
            kwgs = {"code": 200, "msg": "修改成功", 'user': user}
        except Exception as ex:
            logger.error(ex)
            kwgs = {'code': 400, 'msg': '出错了', 'user': user}
        return render(request, 'user_info.html', kwgs)


class UserCommentView(LoginRequiredMixin, View):

    def get(self, request, id):
        user = UserInfo.objects.filter(id=id)
        comments = Comment.objects.filter(user=user).order_by('-comment_time')
        paginator = Paginator(comments, 4)
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        all_pages = range(contacts.paginator.num_pages)
        kwgs = {
            'contacts': contacts,
            'all_pages': all_pages,
        }
        return render(request, 'user_comment.html', kwgs)


class UserCollectionView(LoginRequiredMixin, View):

    def get(self, request, id):
        user = UserInfo.objects.filter(id=id)
        collections = AnimeCollection.objects.filter(user=user, status=True)
        paginator = Paginator(collections, 2)
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        all_pages = range(contacts.paginator.num_pages)
        kwgs = {
            'contacts': contacts,
            'all_pages': all_pages,
        }
        return render(request, 'user_collection.html', kwgs)


class ChangePassword(LoginRequiredMixin, View):

    def post(self, request):
        password1 = request.POST.get('password')
        password2 = request.POST.get('password1')
        user = request.user
        if password1 == password2:
            user.set_password(password1)
            user.save()
            ret = {'status': 200, 'msg': '密码修改成功，请记住新密码哦！'}
            auth.login(request, user)

        else:
            ret = {'status': 400, 'msg': '输入的两个密码不一致'}
        return JsonResponse(ret)
