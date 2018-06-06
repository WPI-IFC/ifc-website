# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-25 02:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('events', '0001_initial'), ('events', '0002_auto_20180523_1949')]

    initial = True

    dependencies = [
        ('houses', '0003_fraternity_motto'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('d_time', models.DateTimeField()),
                ('description', models.TextField()),
                ('splash_img', models.ImageField(upload_to='event_splash/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.Fraternity')),
            ],
            options={
                'abstract': False,
                'ordering': ('-d_time',),
            },
        ),
        migrations.CreateModel(
            name='OfficerEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('d_time', models.DateTimeField()),
                ('description', models.TextField()),
                ('splash_img', models.ImageField(upload_to='event_splash/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'ordering': ('-d_time',),
            },
        ),
    ]