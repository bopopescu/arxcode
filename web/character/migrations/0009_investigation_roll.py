# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-02-11 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0008_auto_20170209_0208'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigation',
            name='roll',
            field=models.SmallIntegerField(blank=True, default=-9999, help_text='Current roll for investigation.'),
        ),
    ]
