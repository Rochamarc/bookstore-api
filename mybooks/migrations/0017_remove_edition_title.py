# Generated by Django 4.0 on 2024-03-20 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mybooks', '0016_edition_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edition',
            name='title',
        ),
    ]