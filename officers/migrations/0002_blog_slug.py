# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-28 23:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default='placeholder-slug'),
            preserve_default=False,
        ),
    ]
