# Generated by Django 4.0.6 on 2022-07-19 18:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]