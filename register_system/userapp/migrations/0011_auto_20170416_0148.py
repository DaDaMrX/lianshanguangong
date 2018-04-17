# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0010_auto_20170416_0141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='email',
        ),
        migrations.RemoveField(
            model_name='person',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='team',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='队长邮箱'),
        ),
        migrations.AddField(
            model_name='team',
            name='phone_number',
            field=models.CharField(max_length=11, null=True, verbose_name='队长手机'),
        ),
    ]
