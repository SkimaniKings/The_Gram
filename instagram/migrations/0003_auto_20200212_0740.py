# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-12 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='roman_reigns.jpg', upload_to=''),
        ),
    ]