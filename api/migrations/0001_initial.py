# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories_100g', models.FloatField(default=0)),
                ('carbs_100g', models.FloatField(default=0)),
                ('fat_100g', models.FloatField(default=0)),
                ('protein_100g', models.FloatField(default=0)),
                ('water_100g', models.FloatField(default=0)),
                ('piece_weight', models.FloatField(default=0)),
                ('calories_unit', models.FloatField(default=0)),
                ('carbs_unit', models.FloatField(default=0)),
                ('fat_unit', models.FloatField(default=0)),
                ('water_unit', models.FloatField(default=0)),
                ('protein_unit', models.FloatField(default=0)),
                ('name', models.CharField(max_length=200)),
                ('trivial', models.CharField(blank=True, max_length=200)),
                ('all_name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
    ]