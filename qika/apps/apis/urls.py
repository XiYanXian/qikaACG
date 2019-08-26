from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get_captcha/$', views.get_captcha, name='get_captcha'),
    url(r'^check_captcha/$', views.check_captcha, name='check_captcha'),
    url(r'^get_email_captcha/$', views.get_email_captcha, name='get_email_captcha'),
    # url(r'^get_tag/(?P<tag>\w+)/$', views.get_tag, name='get_tag'),
    url(r'^anime/judge/(?P<id>\d+)/$', views.JudgeCollection.as_view(), name='anime_judge'),
    url(r'^anime/collection/(?P<id>\d+)/$', views.AnimeCollectionView.as_view(), name='anime_collection'),
    url(r'^comment/like/(?P<id>\d+)/(?P<rank>)\w+$', views.CommentLikeView.as_view(), name='comment_like'),
    url(r'^anime/search/$', views.SearchAnime.as_view(), name='anime_search'),
    url(r'^change_avatar/$', views.ChangeAvatar.as_view(), name='change_avatar'),
]