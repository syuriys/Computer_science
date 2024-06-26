# Generated by Django 4.2.1 on 2023-06-01 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_teacher_additional'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutprogram',
            options={'verbose_name': 'Про програму', 'verbose_name_plural': 'Про програму'},
        ),
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name': 'Контакти', 'verbose_name_plural': 'Контакти'},
        ),
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'Відгук', 'verbose_name_plural': 'Відгук'},
        ),
        migrations.AlterModelOptions(
            name='field',
            options={'verbose_name': 'Поле', 'verbose_name_plural': 'Поля'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новина', 'verbose_name_plural': 'Новини'},
        ),
        migrations.AlterModelOptions(
            name='newsimage',
            options={'verbose_name': 'Зображення новин', 'verbose_name_plural': 'Зображення новин'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Викладач', 'verbose_name_plural': 'Викладачі'},
        ),
        migrations.AlterField(
            model_name='teacher',
            name='additional',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
