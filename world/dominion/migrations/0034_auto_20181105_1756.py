# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-05 17:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exploration', '0003_auto_20181105_1756'),
        ('dominion', '0033_auto_20181105_1756'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Shardhaven',
        ),
        migrations.DeleteModel(
            name='ShardhavenClue',
        ),
        migrations.DeleteModel(
            name='ShardhavenDiscovery',
        ),
        migrations.DeleteModel(
            name='ShardhavenType',
        ),
    ]