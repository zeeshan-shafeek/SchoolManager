# Generated by Django 4.1.7 on 2023-02-16 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=255)),
                ('phone_no', models.CharField(max_length=255)),
                ('details', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('student_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=200, null=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School.school')),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('details', models.CharField(max_length=1000)),
                ('is_completed', models.BooleanField()),
                ('assigned_to', models.ManyToManyField(to='School.student')),
                ('belongs_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('students_enrolled', models.IntegerField()),
                ('students', models.ManyToManyField(to='School.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School.teacher')),
            ],
        ),
    ]
