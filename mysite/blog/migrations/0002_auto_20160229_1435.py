# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 14:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
