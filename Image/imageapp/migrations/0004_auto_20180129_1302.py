# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-29 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0003_auto_20180129_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(blank=True, default=None, upload_to=''),
        ),
    ]
