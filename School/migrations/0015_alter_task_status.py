# Generated by Django 4.1.7 on 2023-03-14 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0014_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Closed', 'Closed')], default='Active', max_length=50, null=True),
        ),
    ]
