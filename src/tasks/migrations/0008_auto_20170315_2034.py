# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_auto_20170315_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categoria',
            field=models.ManyToManyField(to='tasks.Categorias'),
        ),
    ]
