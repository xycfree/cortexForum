# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-11 09:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0006_auto_20160311_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumuser',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 11, 9, 53, 26, 88140, tzinfo=utc)),
        ),
    ]
