# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-09 12:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Independent', max_length=500, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='artistregistered',
            name='label',
            field=models.ForeignKey(default=0, max_length=200, on_delete=django.db.models.deletion.CASCADE, to='music.Label'),
            preserve_default=False,
        ),
    ]
