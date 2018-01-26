# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-26 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0005_auto_20180126_0927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desti', models.CharField(max_length=255)),
                ('descr', models.CharField(max_length=255)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('travelers', models.ManyToManyField(related_name='trips', to='users.User')),
            ],
        ),
    ]
