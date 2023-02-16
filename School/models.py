from django.db import models

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

    def __str__(self):
        return self.roll_number
    def default(self):
        self.roll_number = self.school.name[0:3] + str(self.id)
        self.save()
        
    
    
       
class Course(models.Model):
    name = models.CharField(max_length=100, null= False)
    students_enrolled = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete= models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=50, null= False)
    details = models.CharField(max_length=1000, null= False)
    is_completed = models.BooleanField()
    belongs_to = models.ForeignKey(Teacher, on_delete= models.CASCADE)
    assigned_to = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
