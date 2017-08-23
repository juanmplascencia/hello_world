# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HelloWorld', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='name',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='username',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='users',
            name='datehired',
        ),
        migrations.AddField(
            model_name='users',
            name='last_name',
            field=models.CharField(default='none', max_length=255),
            preserve_default=False,
        ),
    ]
