from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<quater>\d+)/$', views.AnimeQuater.as_view(), name='anime_quater'),
    url(r'^(?P<tag_name>\w+)/$', views.Choice.as_view(), name='tag_index'),
]