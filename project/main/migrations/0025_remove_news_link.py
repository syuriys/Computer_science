# Generated by Django 4.2.1 on 2024-05-12 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_news_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='link',
        ),
    ]
