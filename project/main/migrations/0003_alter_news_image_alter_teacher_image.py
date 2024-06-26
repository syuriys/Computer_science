# Generated by Django 4.2.1 on 2023-05-06 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_contacts_alter_news_image_alter_teacher_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='news_images/'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(upload_to='teachers_images/'),
        ),
    ]
