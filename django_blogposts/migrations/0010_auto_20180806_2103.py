# Generated by Django 2.0.6 on 2018-08-06 21:03

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_blogposts', '0009_auto_20160404_1115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['da'], 'verbose_name': 'Blog post', 'verbose_name_plural': 'Blog posts'},
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='header',
            field=models.CharField(max_length=200, verbose_name='Header (tag H1)'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/%Y/%m/%d', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='meta_kw',
            field=models.CharField(max_length=300, verbose_name='Meta-tag keywords'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='meta_title',
            field=models.CharField(max_length=300, verbose_name='Meta-tag title'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='short_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=1000, null=True, verbose_name='Short content for preview'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=200, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='content',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Short description of category (if needed)'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=200, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=100, verbose_name='Slug'),
        ),
    ]