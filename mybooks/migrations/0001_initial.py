# Generated by Django 4.0 on 2024-03-03 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('published_at', models.CharField(max_length=4, null=True)),
                ('isbn', models.CharField(max_length=20, null=True)),
                ('was_read', models.CharField(max_length=3)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mybooks.author')),
                ('format', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mybooks.format')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mybooks.publisher')),
            ],
        ),
    ]
