# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-26 17:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180126_0747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='birthday',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]
