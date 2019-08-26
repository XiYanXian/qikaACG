from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^detail/(?P<id>\d+)/$', views.AnimeDetail.as_view(), name='anime_detail'),

]