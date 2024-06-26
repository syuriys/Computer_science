# Generated by Django 4.2.1 on 2023-05-09 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_newsimage_remove_news_image_alter_news_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_form', models.TextField(max_length=50)),
                ('licensed_quota', models.IntegerField()),
                ('funded_quota', models.IntegerField()),
                ('subjects', models.TextField()),
                ('tuition_fee', models.IntegerField()),
                ('career_prospects', models.TextField()),
                ('description', models.TextField()),
                ('objects_of_study', models.TextField()),
                ('objectives', models.TextField()),
                ('course_map', models.ImageField(upload_to='course_map_images/')),
            ],
        ),
    ]
