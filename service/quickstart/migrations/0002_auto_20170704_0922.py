# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='cc',
            field=models.BigIntegerField(default=49, help_text='Country code without +'),
        ),
    ]
