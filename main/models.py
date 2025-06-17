from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from datetime import date


class ProfileUser(models.Model):
    ROLE_CHOICES = [
        ('teacher', "O'qituvchi"),
        ('student', "Talaba"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, null=True, blank=True, default='student')

    def __str__(self):
        return f"{self.user.username} - {self.role}"
   
class ProfileInline(admin.StackedInline):
    model = ProfileUser
    can_delete = False
    verbose_name_plural = "Profile"

class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]


class add_professor_model(models.Model):
    
    GENDER_CHOICES = [
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol'),
        ('Boshqa', 'Boshqa')
    ]
    
    full_name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=90)
    birth_date = models.CharField(max_length=90)
    department = models.CharField(max_length=150)
    description = models.TextField()  
    gender = models.CharField(max_length=90, choices=GENDER_CHOICES)     
    
    def __str__(self):
        return self.full_name 

class add_course_model(models.Model):
    name = models.CharField(max_length=150)
    time = models.CharField(max_length=90)
    course_price = models.CharField(max_length=150)
    department = models.CharField(max_length=150)
    description = models.TextField()
    professor = models.ForeignKey(add_professor_model,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
class add_student_model(models.Model):
    
    GENDER_CHOICES = [
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol'),
        ('Boshqa', 'Boshqa')
    ]
    
    full_name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=90)
    birth_date = models.CharField(max_length=90)
    description = models.TextField()  
    gender = models.CharField(max_length=90, choices=GENDER_CHOICES) 
    group = models.ForeignKey(add_course_model,on_delete=models.CASCADE)    
    
    def __str__(self):
        return self.full_name 
    
