# Generated by Django 4.2.1 on 2023-05-25 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_teacher_email_teacher_additional_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='additional',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]