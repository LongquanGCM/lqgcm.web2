# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-23 16:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_title', models.CharField(max_length=200)),
                ('activity_location', models.CharField(default=b'\xe9\xbe\x99\xe6\xb3\x89\xe5\xa4\xa7\xe6\x82\xb2\xe5\xaf\xba', max_length=100)),
                ('activity_date', models.DateTimeField(verbose_name=b'Activity Date')),
                ('activity_text', models.TextField(default=b'to be added', max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='EmailSub',
            fields=[
                ('email_address', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=200)),
                ('event_location', models.CharField(default=b'\xe9\xbe\x99\xe6\xb3\x89\xe5\xa4\xa7\xe6\x82\xb2\xe5\xaf\xba', max_length=100)),
                ('event_date', models.DateTimeField(verbose_name=b'Event Date')),
                ('event_description', models.TextField(default=b'to be added', max_length=1000)),
                ('event_text', models.TextField(default=b'to be added', max_length=2000)),
                ('event_publisher', models.CharField(max_length=100)),
                ('event_publish_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='EventSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_schedule', models.CharField(max_length=200)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_longquan.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Seminar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seminar_topic', models.CharField(max_length=200)),
                ('seminar_location', models.CharField(default=b'Utrecht', max_length=50)),
                ('seminar_date', models.CharField(max_length=50)),
                ('seminar_text', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_member_name', models.CharField(max_length=100)),
                ('team_member_title', models.CharField(max_length=100)),
                ('team_member_photo', models.ImageField(upload_to=b'team/')),
                ('team_member_profile', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Volunteers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_name', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=60)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('zip', models.CharField(max_length=10)),
                ('telephone', models.CharField(max_length=20)),
                ('mobilephone', models.CharField(max_length=20)),
                ('skills', models.CharField(max_length=300)),
                ('contact_message', models.CharField(max_length=300)),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='volunteers',
            unique_together=set([('family_name', 'first_name', 'email')]),
        ),
    ]
