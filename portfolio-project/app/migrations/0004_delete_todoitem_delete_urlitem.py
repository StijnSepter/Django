# Generated by Django 4.2.5 on 2024-01-11 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_slideshow'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TodoItem',
        ),
        migrations.DeleteModel(
            name='urlItem',
        ),
    ]
