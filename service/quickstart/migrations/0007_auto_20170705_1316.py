# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-05 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0006_auto_20170705_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='origin',
            field=models.CharField(default='', help_text='Phone number of WhatsApp account owner - ignored for now.', max_length=30),
        ),
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[('U', 'Unsend'), ('S', 'Sent'), ('A', 'Acknowledged'), ('E', 'Error occured trying to send message')], default='U', max_length=1),
        ),
    ]
