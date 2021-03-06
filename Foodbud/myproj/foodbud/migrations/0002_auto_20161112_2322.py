# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 04:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodbud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(default='', max_length=50)),
                ('brand_id', models.CharField(default='', max_length=50)),
                ('brand_name', models.CharField(default='', max_length=37)),
                ('item_name', models.CharField(default='', max_length=80)),
                ('price', models.FloatField()),
                ('category', models.CharField(default='', max_length=7)),
                ('item_description', models.TextField(default='')),
                ('calories', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]
