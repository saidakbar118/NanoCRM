# Generated by Django 5.1.1 on 2025-06-25 06:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_profileuser_is_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_student_model',
            name='group',
        ),
        migrations.RemoveField(
            model_name='add_student_model',
            name='user',
        ),
        migrations.AlterField(
            model_name='payment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profileuser'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profileuser'),
        ),
        migrations.DeleteModel(
            name='add_professor_model',
        ),
        migrations.DeleteModel(
            name='add_student_model',
        ),
    ]
