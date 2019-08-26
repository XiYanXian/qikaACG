# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-20 06:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReleaseDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('play_date', models.CharField(max_length=10, verbose_name='番剧季度')),
            ],
            options={
                'verbose_name': '番剧季度时间',
                'verbose_name_plural': '番剧季度时间',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=10, verbose_name='标签名')),
                ('tag_url', models.CharField(max_length=10, verbose_name='标签的路由名')),
            ],
            options={
                'verbose_name': '标签列表',
                'verbose_name_plural': '标签列表',
            },
        ),
    ]