# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-19 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='capwedget',
            name='available_supply',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='capwedget',
            name='last_update',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='capwedget',
            name='max_supply',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='capwedget',
            name='percent_change_1h',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='capwedget',
            name='percent_change_24h',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='capwedget',
            name='percent_change_7d',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='capwedget',
            name='symbol',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='capwedget',
            name='total_supply',
            field=models.TextField(null=True),
        ),
    ]