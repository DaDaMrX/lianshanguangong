# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 03:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_auto_20170414_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='captain',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userapp.Person', verbose_name='队长'),
        ),
    ]