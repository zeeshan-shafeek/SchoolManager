# Generated by Django 4.1.7 on 2023-03-14 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0013_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default='Active', max_length=50, null=True),
        ),
    ]