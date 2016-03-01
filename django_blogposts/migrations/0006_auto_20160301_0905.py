# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-01 09:05
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_blogposts', '0005_blogpost_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, max_length=100, populate_from=b'name', verbose_name='Slug')),
                ('is_moderated', models.BooleanField(default=True, verbose_name='Is moderated')),
                ('da', models.DateTimeField(auto_now_add=True, verbose_name='Date of create')),
                ('de', models.DateTimeField(auto_now=True, verbose_name='Date of last edit')),
            ],
            options={
                'ordering': ['-da'],
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='blogpost',
            name='tags',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_blogposts.Tags', verbose_name='tags'),
        ),
    ]