# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 00:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_auto_20160228_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productot',
            name='message',
        ),
    ]
