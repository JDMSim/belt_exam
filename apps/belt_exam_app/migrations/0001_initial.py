# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 22:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginRegistration_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('goers', models.ManyToManyField(related_name='all_users', to='loginRegistration_app.User')),
                ('planner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginRegistration_app.User')),
            ],
        ),
    ]
