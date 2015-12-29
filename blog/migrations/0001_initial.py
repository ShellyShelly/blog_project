# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('summary', models.TextField(default=b'', blank=True)),
                ('content', models.TextField(default=b'', blank=True)),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]
