# Generated by Django 4.1.7 on 2023-02-18 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0006_remove_course_students_enrolled'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='belongs_to',
            new_name='course',
        ),
        migrations.RemoveField(
            model_name='task',
            name='assigned_to',
        ),
    ]