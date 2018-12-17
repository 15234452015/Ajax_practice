# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-16 13:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clazz',
            fields=[
                ('cno', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=20)),
                ('clazz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stu.Clazz')),
            ],
        ),
    ]
