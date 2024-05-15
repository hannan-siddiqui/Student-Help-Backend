# Generated by Django 5.0.4 on 2024-05-09 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_student_email_alter_student_rollno'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.TextField(default='MCA', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='desc',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='github',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photo/'),
        ),
        migrations.AddField(
            model_name='student',
            name='linkedin',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.TextField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='skills',
            field=models.TextField(max_length=500, null=True),
        ),
    ]