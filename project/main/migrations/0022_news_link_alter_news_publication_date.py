# Generated by Django 4.2.1 on 2024-05-12 20:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_news_publication_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='publication_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
