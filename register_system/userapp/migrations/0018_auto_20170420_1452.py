# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0017_auto_20170419_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='clothing_size',
            field=models.CharField(choices=[('XS', 'XS，身高160cm'), ('S', 'S，身高165cm'), ('M', 'M，身高170cm'), ('L', 'L，身高175cm'), ('XL', 'XL，身高180cm'), ('XXL', 'XXL，身高185cm')], max_length=4, verbose_name='衣服尺码'),
        ),
        migrations.AlterField(
            model_name='person',
            name='grade',
            field=models.CharField(max_length=5, verbose_name='年级，1-4分别表示大一至大四，5为研一，6为博一'),
        ),
    ]
