# Generated by Django 4.1.7 on 2023-03-03 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='account_type',
            field=models.CharField(choices=[('ADMIN', 'Administrator'), ('TEACHER', 'Teacher'), ('STUDENT', 'Student')], default='STUDENT', max_length=50),
        ),
    ]
