from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    ADMIN = 'ADMIN'
    TEACHER = 'TEACHER'
    STUDENT = 'STUDENT'

    user_types =   (

    (ADMIN , 'Administrator'),
    (TEACHER, 'Teacher'),
    (STUDENT, 'Student'),
    
    )

    account_type = models.CharField(max_length=50, null= False, blank= False, choices= user_types, default= "Student")
