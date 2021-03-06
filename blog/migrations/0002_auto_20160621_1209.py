# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-21 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0002_auto_20160621_1209'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='startup',
        ),
        migrations.AddField(
            model_name='post',
            name='startups',
            field=models.ManyToManyField(related_name='blog_posts', to='organizer.Startup'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text='label for URL config.', max_length=63, unique_for_month='pub date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=63),
        ),
    ]
