# Generated by Django 4.1.7 on 2023-02-18 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0007_rename_belongs_to_task_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='is_completed',
        ),
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School.student')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School.task')),
            ],
        ),
    ]