# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-06-12 09:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ihr', '0004_auto_20161206_0623'),
    ]

    operations = [
        migrations.CreateModel(
            name='country',
            fields=[
                ('code', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Disco_events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('streamtype', models.CharField(max_length=10)),
                ('streamname', models.CharField(max_length=10)),
                ('start', models.DateTimeField(db_index=True)),
                ('end', models.DateTimeField(db_index=True)),
                ('avglevel', models.FloatField(default=0.0)),
                ('totalprobes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Disco_probes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('probe_id', models.IntegerField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('level', models.FloatField(default=0.0)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ihr.Disco_events')),
            ],
        ),
    ]
