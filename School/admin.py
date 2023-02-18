from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Course)


class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ['assigned_tasks']

admin.site.register(Student, StudentAdmin)


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ['assigned_students']

admin.site.register(Task, TaskAdmin)