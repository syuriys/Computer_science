# Generated by Django 4.2.1 on 2023-05-25 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_field_remove_aboutprogram_career_prospects_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutprogram',
            name='main_img',
            field=models.ImageField(blank=True, null=True, upload_to='main_images/'),
        ),
    ]