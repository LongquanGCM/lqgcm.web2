# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-15 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_longquan', '0019_auto_20170815_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_source',
            field=models.CharField(default=b'', max_length=200, verbose_name=b'\xe4\xbf\xa1\xe6\x81\xaf\xe6\x9d\xa5\xe6\xba\x90\xef\xbc\x88\xe5\x8f\xaf\xe9\x80\x89\xef\xbc\x89'),
        ),
    ]
