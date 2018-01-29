# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-29 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0002_auto_20180128_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(blank=True, default=None, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
    ]
