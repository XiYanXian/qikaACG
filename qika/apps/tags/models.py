from django.db import models

# Create your models here.


class Tags(models.Model):
    tag_name = models.CharField(max_length=10, verbose_name='标签名')
    tag_url = models.CharField(max_length=10, verbose_name='标签的路由名')

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = '标签列表'
        verbose_name_plural = verbose_name


class ReleaseDate(models.Model):
    play_date = models.CharField(max_length=10, verbose_name='番剧季度')

    def __str__(self):
        return self.play_date

    class Meta:
        verbose_name = '番剧季度时间'
        verbose_name_plural = verbose_name
