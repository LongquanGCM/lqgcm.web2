# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-27 16:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_longquan', '0014_comment_comment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='app_longquan.Comment'),
        ),
    ]