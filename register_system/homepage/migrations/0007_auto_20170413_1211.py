# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_homepageimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepageimage',
            name='title',
            field=models.TextField(default='', verbose_name='图片介绍'),
        ),
        migrations.AlterField(
            model_name='homepageimage',
            name='image',
            field=models.ImageField(null=True, upload_to='img/', verbose_name='滚动图片'),
        ),
        migrations.AlterField(
            model_name='noticefile',
            name='file',
            field=models.FileField(null=True, upload_to='file/', verbose_name='附件'),
        ),
    ]
