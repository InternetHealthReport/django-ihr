# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-08-17 01:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ihr', '0021_forwarding_alarms_msms_forwarding_alarms_probes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Congestion',
            new_name='Delay',
        ),
        migrations.RenameModel(
            old_name='Congestion_alarms',
            new_name='Delay_alarms',
        ),
        migrations.RenameModel(
            old_name='Congestion_alarms_msms',
            new_name='Delay_alarms_msms',
        ),
        migrations.RenameModel(
            old_name='Congestion_alarms_probes',
            new_name='Delay_alarms_probes',
        ),
        migrations.RenameModel(
            old_name='CongestionRanking',
            new_name='DelayRanking',
        ),
    ]
