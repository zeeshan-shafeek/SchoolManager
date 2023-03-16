from django.forms import ModelForm
from School.models import Task, Course

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        
class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
