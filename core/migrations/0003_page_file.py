# Generated by Django 4.1.7 on 2023-03-18 05:35

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_chapter_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='file',
            field=models.ImageField(default='', upload_to=core.models.Page.file_path),
            preserve_default=False,
        ),
    ]
