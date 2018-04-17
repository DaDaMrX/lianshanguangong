# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0012_auto_20170416_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True, verbose_name='队长邮箱'),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=10, unique=True, verbose_name='队伍名称'),
        ),
    ]