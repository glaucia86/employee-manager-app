# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('birthday', models.DateField()),
                ('phone', models.CharField(max_length=12)),
                ('address', models.TextField()),
            ],
        ),
    ]
