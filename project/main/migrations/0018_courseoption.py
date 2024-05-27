# Generated by Django 4.2.1 on 2024-04-30 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_course_page_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва курсу')),
                ('page_link', models.URLField(verbose_name='Посилання на курс')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='main.course')),
            ],
        ),
    ]
