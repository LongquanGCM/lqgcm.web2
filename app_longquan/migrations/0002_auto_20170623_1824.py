# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-23 16:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_longquan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventschedule',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_schedule', to='app_longquan.Event'),
        ),
    ]
