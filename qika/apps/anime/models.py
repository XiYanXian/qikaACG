from django.db import models
from apps.tags.models import Tags, ReleaseDate
from easy_thumbnails.fields import ThumbnailerImageField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class VoiceActor(models.Model):
    voice_actor_name = models.CharField(max_length=50, verbose_name='声优名')

    def __str__(self):
        return self.voice_actor_name

    class Meta:
        verbose_name = '声优'
        verbose_name_plural = verbose_name


class Staff(models.Model):
    staff_name = models.CharField(max_length=50, verbose_name='公司名')

    def __str__(self):
        return self.staff_name

    class Meta:
        verbose_name = '会社'
        verbose_name_plural = verbose_name


class Supervision(models.Model):
    supervision_name = models.CharField(max_length=50, verbose_name='监督名')

    def __str__(self):
        return self.supervision_name

    class Meta:
        verbose_name = '监督'
        verbose_name_plural = verbose_name


class Musician(models.Model):
    musician_name = models.CharField(max_length=512, verbose_name='音乐')

    def __str__(self):
        return self.musician_name

    class Meta:
        verbose_name = '音乐'
        verbose_name_plural = verbose_name


# class AnimeUpdateTime(models.Model):
#     update_time = models.CharField(max_length=128, verbose_name='更新时间')
#
#     def __str__(self):
#         return self.update_time
#
#     class Meta:
#         verbose_name = '更新时间'
#         verbose_name_plural = verbose_name
#
#
class AnimeTimeWeek(models.Model):
    play_time = models.CharField(max_length=10, verbose_name='每周播放时间')

    def __str__(self):
        return self.play_time

    class Meta:
        verbose_name = '每周播放时间'
        verbose_name_plural = verbose_name


class AnimeList(models.Model):
    anime_name = models.CharField(max_length=50, verbose_name='番剧名')
    tags = models.ManyToManyField(Tags, verbose_name='标签')
    anime_intro = RichTextUploadingField(verbose_name='番剧简介', null=True, blank=True)
    release_date = models.ManyToManyField(ReleaseDate, verbose_name='番剧日期')
    staff = models.ManyToManyField(Staff, verbose_name='制作公司')
    musician = models.ManyToManyField(Musician, verbose_name='音乐')
    supervision = models.ManyToManyField(Supervision, verbose_name='监督名')
    n_point = models.IntegerField(verbose_name='点击量', null=True, blank=True, default=0)
    n_collection = models.IntegerField(verbose_name='收藏量', null=True, blank=True, default=0)
    website = RichTextUploadingField(max_length=512, verbose_name='播放网站', null=True, blank=True)
    anime_image = ThumbnailerImageField(upload_to='anime_pic/', verbose_name='番剧图片')
    anime_image_small = ThumbnailerImageField(upload_to='anime_pic/', verbose_name='番剧小图')
    episode_num = models.IntegerField(verbose_name='番剧集数')
    anime_time_week = models.ForeignKey(AnimeTimeWeek, verbose_name='每周播放时间')

    def __str__(self):
        return self.anime_name

    class Meta:
        verbose_name = '番剧'
        verbose_name_plural = verbose_name
        ordering = ['n_point']


class Character(models.Model):
    id = models.AutoField(primary_key=True)
    anime = models.ForeignKey(AnimeList, verbose_name='番剧名')
    character_name = models.CharField(max_length=50, verbose_name='角色名')
    character_image = ThumbnailerImageField(upload_to='character_pic', max_length=50, verbose_name='角色图片路径')
    voice_actor = models.ForeignKey(VoiceActor, verbose_name='配音的声优')
    character_intro = RichTextUploadingField(max_length=512, verbose_name='角色介绍')

    def __str__(self):
        return self.character_name

    class Meta:
        verbose_name = '主要角色'
        verbose_name_plural = verbose_name







