# Generated by Django 4.1.7 on 2023-02-18 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0005_alter_task_belongs_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='students_enrolled',
        ),
    ]