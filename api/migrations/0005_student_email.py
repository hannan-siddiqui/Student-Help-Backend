# Generated by Django 5.0.4 on 2024-05-06 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_student_course_remove_student_desc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
