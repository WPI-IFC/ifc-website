# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-20 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_auto_20171005_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='fraternity',
            name='motto',
            field=models.TextField(blank=True),
        ),
    ]
