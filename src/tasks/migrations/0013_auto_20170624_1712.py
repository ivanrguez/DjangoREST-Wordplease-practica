# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-24 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_auto_20170624_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categoria',
            field=models.ManyToManyField(to='tasks.Categorias'),
        ),
    ]
