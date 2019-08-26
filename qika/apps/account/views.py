# Create your views here.
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views.generic import View
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.hashers import make_password
import logging
import random
import string
from apps.users.models import UserInfo
from django.core.cache import cache
from django.core.mail import send_mail, EmailMultiAlternatives
from qika.settings import EMAIL_FROM
from django.core.cache import cache
logger = logging.getLogger('account')


# Create your views here.

class Register(View):
    def get(self, request):
        return redirect(reverse('index'))

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        nickname = request.POST.get('nickname')
        email = request.POST.get('email')
        email_captcha = request.POST.get('email_captcha')
        if_username_exist = UserInfo.objects.filter(username=username)
        if_nickname_exist = UserInfo.objects.filter(nickname=nickname)
        if_email_exist = UserInfo.objects.filter(email=email)
        email_captcha_redis = cache.get(email)
        if not if_username_exist and not if_nickname_exist and not if_email_exist \
                and (password == password2) and (email_captcha == email_captcha_redis):
            user = UserInfo.objects.create(username=username, password=make_password(password),
                                           nickname=nickname, email=email)
            user.save()
            auth.login(request, user)
            ret = {'status': 200, 'msg': '用户注册成功'}
        elif if_username_exist:
            ret = {'status': 402, 'msg': '账号已存在'}
        elif if_nickname_exist:
            ret = {'status': 402, 'msg': '昵称已存在'}
        elif if_email_exist:
            ret = {'status': 402, 'msg': '邮箱已存在'}
        elif password != password2:
            ret = {'status': 402, 'msg': '两次密码不一致'}
        elif email_captcha != email_captcha_redis:
            ret = {'status': 402, 'msg': '邮箱验证码不正确'}
        elif not email_captcha_redis:
            ret = {'status': 401, 'msg': '验证码错误或过期'}
        else:
            ret = {'status': 400, 'msg': '调用方式错误'}
        return JsonResponse(ret)


class Login(View):

    def get(self, request):
        return redirect(reverse('index'))

    # Form表单直接提交
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        captcha = request.POST.get('captcha')
        session_captcha_code = request.session.get('captcha_code', '')
        if captcha.lower() == session_captcha_code.lower():
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                logger.info(f"{user.username}登录成功")
                ret = {'status': 200, 'msg': '登录成功'}
            else:

                logger.error(f"{username}登录失败, 用户名或密码错误")
                ret = {'status': 400, 'msg': '账号或密码错误'}
        else:
            ret = {'status': 400, 'msg': '验证码错误'}
            logger.error(f'{username}登陆失败，验证码错误')
        return JsonResponse(ret)


def logout(request):
    auth.logout(request)
    return redirect(reverse('index'))


class PasswordForget(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        if username and email and UserInfo.objects.filter(
                username=username, email=email):
            verify_code = "".join(
                random.choices(
                    string.ascii_lowercase +
                    string.digits,
                    k=128))
            url = f"{request.scheme}://{request.META['HTTP_HOST']}/account/password/reset/{verify_code}?email={email}"
            cache.set(verify_code,
                      {'username': username,
                       'email': email,
                       'verify_code': verify_code,
                       'url': url},
                      1800)
            email_title = '【qikaACG】忘记密码验证'
            email_body = f'<p>点击下面的链接进行验证，有效时间30分钟：</p></br><a href="{url}">{url}</a>'
            msg = EmailMultiAlternatives(
                email_title, email_body, EMAIL_FROM, [email])
            msg.content_subtype = "html"
            msg.send()
            ret = {'status': 200, 'msg': '邮件发送成功，请登录邮箱查看！如果没收到，请到垃圾箱查看是否存在！'}
        else:
            ret = {'status': 400, 'msg': '输入的邮箱不存在！'}
        return JsonResponse(ret)


class PasswordReset(View):
    def get(self, request, verify_code):
        message = cache.get(verify_code)
        if verify_code and message:
            return render(request, 'password_reset.html')
        else:
            return HttpResponse("链接失效或有误")

    def post(self, request, verify_code):
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            try:
                message = cache.get(verify_code)
                email = message.get('email')
                user = UserInfo.objects.get(email=email)
                user.set_password(password1)
                user.save()
                msg = "重置密码成功"
                code = 200
            except Exception as ex:
                logger.error(ex)
                code = 400
                msg = "出错啦"
        else:
            code = 400
            msg = '两次密码不一致'
        return render(request, 'password_reset.html', {'code': code, 'msg': msg})


def page_not_found(request):
    return render(request, '404.html')