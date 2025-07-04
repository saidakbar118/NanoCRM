# Generated by Django 5.1.1 on 2025-06-14 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_add_professor_model_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_course_model',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='add_course_model',
            name='image',
        ),
        migrations.RemoveField(
            model_name='add_course_model',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='add_course_model',
            name='year',
        ),
        migrations.RemoveField(
            model_name='add_professor_model',
            name='image',
        ),
        migrations.AddField(
            model_name='add_course_model',
            name='time',
            field=models.CharField(default=1, max_length=90),
            preserve_default=False,
        ),
    ]
