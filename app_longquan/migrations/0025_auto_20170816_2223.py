# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-16 20:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_longquan', '0024_auto_20170816_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seminarenroll',
            name='seminar',
        ),
        migrations.DeleteModel(
            name='Seminar',
        ),
        migrations.DeleteModel(
            name='SeminarEnroll',
        ),
    ]