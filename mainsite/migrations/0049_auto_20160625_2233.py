# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 17:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0048_auto_20160625_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='DOB',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 6, 25, 17, 3, 10, 134661, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='pic',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
