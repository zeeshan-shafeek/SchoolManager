from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=50, null= False)
    Address = models.CharField(max_length=255, null= False)
    phone_no = models.CharField(max_length=255, null= False)
    details = models.CharField(max_length=1000, null= False)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=50, null= False)
    title = models.CharField(max_length=200, null= False)
    details = models.CharField(max_length=200, null= True, blank= True)
    school = models.ForeignKey(School, on_delete= models.CASCADE)

    def __str__(self):
        return (self.name + " ("+ self.title + ")")



class Student(models.Model):
          
    name = models.CharField(max_length=50, null= False)
    school = models.ForeignKey(School, on_delete= models.CASCADE)
    roll_number = models.CharField(max_length= 10, null= False, blank= True)
    
    def assigned_tasks(self):
        tasks = Task.objects.filter(course__students = self)
        if tasks:
            status = ''
            for student_task in tasks:
                stauts = TaskStatus.objects.filter(task=student_task, student= self)
                if stauts:
                    status = ' (Done)'
                else:
                    status = ' (Incomplete)'

            tasks = ', '.join([student_task.name + status])
                
            return tasks
        else:
            return 'None'
    
    assigned_tasks.short_description = 'Assigned Tasks'


    def __str__(self):
       return self.roll_number
    
    # to automatically assign roll number to the student
    def save(self, *args, **kwargs):
            if not self.roll_number:
                school_name_prefix = self.school.name[:3].upper()
                last_student_for_school = Student.objects.filter(school=self.school).order_by('-id').first()
                if last_student_for_school:
                    last_roll_number = int(last_student_for_school.roll_number.split('-')[1])
                else:
                    last_roll_number = 0
                self.roll_number = f"{school_name_prefix}-{last_roll_number+1:03d}"
            super().save(*args, **kwargs)
   
    
    
       
class Course(models.Model):
    name = models.CharField(max_length=100, null= False)
    #students_enrolled = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete= models.CASCADE)
    students = models.ManyToManyField(Student)
       
    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=50, null= False)
    details = models.CharField(max_length=1000, null= False)
    # is_completed = models.BooleanField(default=False)
    course = models.ForeignKey(Course, on_delete= models.CASCADE)

    def __str__(self):
        return self.name

    def assigned_students(self):
        return ', '.join([str(student) for student in self.course.students.all()])

    assigned_students.short_description = 'Assigned Students'

class TaskStatus(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete= models.CASCADE)
    status = models.BooleanField(default= False)




