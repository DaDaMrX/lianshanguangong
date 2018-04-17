# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 04:25
from __future__ import unicode_literals

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_auto_20170419_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='contact_us',
            field=djrichtextfield.models.RichTextField(blank=True, null=True, verbose_name='联系我们内容'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='简短描述'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='title_top',
            field=models.TextField(blank=True, null=True, verbose_name='抬头标题'),
        ),
    ]
