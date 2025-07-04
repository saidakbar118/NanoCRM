# Generated by Django 5.1.1 on 2025-06-19 06:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_add_professor_model_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_professor_model',
            name='user',
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.add_course_model')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.add_student_model')),
            ],
            options={
                'unique_together': {('student', 'course', 'date')},
            },
        ),
    ]
