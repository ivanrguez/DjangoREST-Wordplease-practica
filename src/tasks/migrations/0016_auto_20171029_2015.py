# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-29 19:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0015_auto_20171029_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tasks.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categoria',
            field=models.ManyToManyField(to='tasks.Categorias'),
        ),
    ]
