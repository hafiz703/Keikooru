# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20161208_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistregistered',
            name='picture',
            field=models.CharField(max_length=200),
        ),
    ]
