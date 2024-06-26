# Generated by Django 4.2.1 on 2024-05-14 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_news_options_alter_teacher_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-semester'], 'verbose_name': 'Курс', 'verbose_name_plural': 'Курси'},
        ),
        migrations.RemoveField(
            model_name='aboutprogram',
            name='description',
        ),
        migrations.RemoveField(
            model_name='aboutprogram',
            name='objectives',
        ),
        migrations.RemoveField(
            model_name='aboutprogram',
            name='objects_of_study',
        ),
        migrations.CreateModel(
            name='SpecialtyFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('about_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='main.aboutprogram')),
            ],
            options={
                'verbose_name': 'Особливість спеціальності',
                'verbose_name_plural': 'Особливості спеціальності',
            },
        ),
    ]
