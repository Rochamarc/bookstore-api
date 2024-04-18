# Generated by Django 4.0 on 2024-04-18 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mymangas', '0008_rename_author_mangaauthor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authormanga',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manga', to='mymangas.mangaauthor'),
        ),
        migrations.AlterField(
            model_name='authormanga',
            name='manga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='mymangas.manga'),
        ),
    ]
