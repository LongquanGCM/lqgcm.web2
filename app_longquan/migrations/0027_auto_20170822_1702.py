# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-22 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_longquan', '0026_speaker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speaker',
            name='activity',
        ),
        migrations.AddField(
            model_name='speaker',
            name='activity',
            field=models.ManyToManyField(related_name='speakers', to='app_longquan.Activity'),
        ),
    ]
