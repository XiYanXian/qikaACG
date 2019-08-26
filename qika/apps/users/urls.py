"""
@file:   urls.py
@date:   2019/07/29
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^info/(?P<id>\d+)/$', views.UserCenter.as_view(), name='info'),
    url(r'^comment/(?P<id>\d+)/$', views.UserCommentView.as_view(), name='comment'),
    url(r'^collection/(?P<id>\d+)/$', views.UserCollectionView.as_view(), name='collection'),
    url(r'^change_pwd/$', views.ChangePassword.as_view(), name='change_pwd'),
]