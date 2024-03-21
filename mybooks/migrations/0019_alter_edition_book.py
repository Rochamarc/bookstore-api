# Generated by Django 4.0 on 2024-03-21 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mybooks', '0018_remove_book_format_remove_book_isbn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edition',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_editions', to='mybooks.book'),
        ),
    ]