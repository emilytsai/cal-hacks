# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('life', models.IntegerField(default=10)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-life', 'name'],
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=250)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='item',
            name='stock',
            field=models.ForeignKey(to='mainpage.List'),
        ),
    ]
