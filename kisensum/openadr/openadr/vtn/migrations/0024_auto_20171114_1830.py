# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-14 18:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vtn', '0023_auto_20171114_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportedReports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_specifier_id', models.CharField(blank=True, max_length=100, null=True)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vtn.Site')),
            ],
        ),
        migrations.AlterField(
            model_name='drevent',
            name='last_status_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 11, 14, 18, 30, 49, 553883), null=True, verbose_name='Last Status Time'),
        ),
        migrations.AlterField(
            model_name='siteevent',
            name='last_opt_in',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 11, 14, 18, 30, 49, 555231), null=True, verbose_name='Last opt-in'),
        ),
        migrations.AlterField(
            model_name='siteevent',
            name='last_status_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 14, 18, 30, 49, 555126), verbose_name='Last Status Time'),
        ),
    ]
