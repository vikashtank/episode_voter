# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-16 20:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='names',
            new_name='name',
        ),
    ]