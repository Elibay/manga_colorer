# Generated by Django 4.1.7 on 2023-03-18 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='number',
            field=models.PositiveIntegerField(default=1),
        ),
    ]