# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 06:52
from __future__ import unicode_literals

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_auto_20170419_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='content',
            field=froala_editor.fields.FroalaField(),
        ),
    ]