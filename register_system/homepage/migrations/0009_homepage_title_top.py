# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 04:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_homepage_contact_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='title_top',
            field=models.TextField(default='', verbose_name='抬头标题'),
            preserve_default=False,
        ),
    ]
