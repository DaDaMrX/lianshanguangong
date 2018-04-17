# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20170413_0216'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': '主页设置', 'verbose_name_plural': '主页设置'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='description',
            field=models.TextField(default='', verbose_name='简短描述'),
            preserve_default=False,
        ),
    ]
