# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0007_auto_20170415_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='邮件'),
        ),
    ]
