# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-01 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_religion', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Religiones',
            },
        ),
    ]
