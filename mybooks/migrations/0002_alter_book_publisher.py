# Generated by Django 4.0 on 2024-03-04 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mybooks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mybooks.publisher'),
        ),
    ]
