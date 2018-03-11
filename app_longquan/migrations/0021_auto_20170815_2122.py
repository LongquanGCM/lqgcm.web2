# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-15 19:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_longquan', '0020_auto_20170815_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_photo',
            field=models.ImageField(blank=True, default=b'', upload_to=b'activities/', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xef\xbc\x88\xe5\x8f\xaf\xe9\x80\x89\xef\xbc\x89'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_publish_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f\xef\xbc\x88\xe5\x8f\xaf\xe9\x80\x89\xef\xbc\x89'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_publisher',
            field=models.CharField(blank=True, default=b'', max_length=100, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe8\x80\x85\xef\xbc\x88\xe5\x8f\xaf\xe9\x80\x89\xef\xbc\x89'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_source',
            field=models.CharField(blank=True, default=b'', max_length=200, verbose_name=b'\xe4\xbf\xa1\xe6\x81\xaf\xe6\x9d\xa5\xe6\xba\x90\xef\xbc\x88\xe5\x8f\xaf\xe9\x80\x89\xef\xbc\x89'),
        ),
    ]