from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.anime.models import AnimeList
from easy_thumbnails.fields import ThumbnailerImageField
# Create your models here.
sex_choices = (
    (0, '男'),
    (1, '女'),
    (2, '保密')
)


class UserInfo(AbstractUser):
    nickname = models.CharField(unique=True, max_length=12, verbose_name='昵称')
    email = models.EmailField(unique=True, max_length=32, verbose_name='邮箱')
    intro = models.CharField(max_length=256, verbose_name='简介', null=True, blank=True)
    sex = models.IntegerField(verbose_name='性别', choices=sex_choices, null=True, blank=True, default=2)
    icon = ThumbnailerImageField(upload_to='icon/', default='images/default.png', verbose_name='头像')


    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户列表"
        verbose_name_plural = verbose_name


class Comment(models.Model):
    user = models.ForeignKey(UserInfo, verbose_name='评论人')
    anime = models.ForeignKey(AnimeList, verbose_name='番剧')
    content = models.CharField(max_length=256, verbose_name='评论内容')
    comment_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    n_like = models.IntegerField(verbose_name='点赞数', blank=True, null=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name


class AnimeCollection(models.Model):
    anime = models.ForeignKey(AnimeList, verbose_name='番剧')
    user = models.ForeignKey(UserInfo, verbose_name='收藏者')
    create_time = models.DateTimeField('收藏/取消时间', auto_now=True)
    # True表示收藏， False表示未收藏
    status = models.BooleanField('收藏状态', default=True)

    class Meta:
        verbose_name = '收藏记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.status:
            ret = '收藏'
        else:
            ret = '取消收藏'
        return f'{self.user}:{ret}:{self.anime.anime_name}'


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, verbose_name='评论')
    user = models.ForeignKey(UserInfo, verbose_name='点赞人')
    create_time = models.DateTimeField('点赞/取消时间', auto_now=True)
    # True表示收藏， False表示未收藏
    status = models.BooleanField('点赞状态', default=True)

    class Meta:
        verbose_name = '点赞记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.status:
            ret = '点赞'
        else:
            ret = '取消点赞'
        return f'{self.user}:{ret}:{self.comment.content}'