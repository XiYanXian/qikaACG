from django.shortcuts import render
from django.views.generic import View
from .models import Tags, ReleaseDate
from apps.anime.models import AnimeList
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class Choice(View):
    def get(self, request, tag_name):
        tags = Tags.objects.all()
        this_tag = Tags.objects.filter(tag_url=tag_name)
        if this_tag:
            anime_list = AnimeList.objects.filter(tags=this_tag)
            tag = Tags.objects.get(tag_url=tag_name).tag_name
        else:
            anime_list = AnimeList.objects.all()
            tag = '所有番剧'
        paginator = Paginator(anime_list, 4)
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        anime_rank = anime_list.order_by('-n_point')[:5]
        all_pages = range(contacts.paginator.num_pages)
        kwgs = {
            'tag': tag,
            'tags': tags,
            'anime_list': anime_list,
            'anime_rank': anime_rank,
            'contacts': contacts,
            'all_pages': all_pages,
        }

        return render(request, 'tag_detail.html', kwgs)


# 番剧季度
class AnimeQuater(View):

    def get(self, request, quater):
        this_quater = ReleaseDate.objects.filter(play_date=quater)
        animes = AnimeList.objects.filter(release_date=this_quater)
        anime_year = quater[:4]
        anime_month = quater[4:]
        paginator = Paginator(animes, 5)
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        all_pages = range(contacts.paginator.num_pages)
        kwgs ={
            'animes': animes,
            'anime_year': anime_year,
            'anime_month': anime_month,
            'contacts': contacts,
            'all_pages': all_pages,
        }
        return render(request, 'anime_quater.html', kwgs)