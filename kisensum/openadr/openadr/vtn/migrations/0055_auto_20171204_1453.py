# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-04 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vtn', '0054_auto_20171204_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='ven_id',
            field=models.CharField(default='venidcuplicate', max_length=100, unique=True, verbose_name='VEN ID'),
            preserve_default=False,
        ),
    ]
