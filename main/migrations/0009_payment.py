# Generated by Django 5.1.1 on 2025-06-19 06:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_add_professor_model_user_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_paid', models.BooleanField(default=True)),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.add_course_model')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.add_student_model')),
            ],
            options={
                'unique_together': {('student', 'course', 'month')},
            },
        ),
    ]
