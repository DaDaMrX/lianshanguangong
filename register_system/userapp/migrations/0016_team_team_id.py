# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0015_auto_20170416_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_id',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
