# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 00:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_productot_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='productot',
            name='message2',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
