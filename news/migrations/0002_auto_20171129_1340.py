# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 13:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('datetime',)},
        ),
        migrations.RemoveField(
            model_name='news',
            name='created',
        ),
    ]