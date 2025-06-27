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
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    full_name = models.CharField(max_length=150, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    phone_number = models.CharField(max_length=90, null=True, blank=True)
    birth_date = models.CharField(max_length=90, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    department = models.CharField(max_length=150, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    group = models.ForeignKey('add_course_model', on_delete=models.SET_NULL, null=True, blank=True)

    # ✅ Yangi maydon: tasdiqlanganmi?
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name



class add_course_model(models.Model):
    name = models.CharField(max_length=150)
    time = models.CharField(max_length=90)
    course_price = models.CharField(max_length=150)
    department = models.CharField(max_length=150)
    description = models.TextField()
    days = models.CharField(max_length=200)

    # faqat 'teacher' roledagi ProfileUser bo'lishi kerak
    professor = models.ForeignKey('ProfileUser', on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'})

    def __str__(self):
        return self.name
   
   
   
class ProfileInline(admin.StackedInline):
    model = ProfileUser
    can_delete = False
    verbose_name_plural = "Profile"

class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]

    
    
class Attendance(models.Model):
    student = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    course = models.ForeignKey(add_course_model, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField(default=False)  # True = qatnashdi

    class Meta:
        unique_together = ('student', 'course', 'date')

    def __str__(self):
        return f"{self.student.full_name} - {self.date} - {'Bor' if self.status else 'Yo‘q'}"
    
class Payment(models.Model):
    student = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    course = models.ForeignKey(add_course_model, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)  # "Iyun 2025" kabi
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=True)
    payment_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course', 'month')

    def __str__(self):
        return f"{self.student.full_name} - {self.month} - {'To‘landi' if self.is_paid else 'To‘lanmagan'}"
  
  

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Xabar: {self.user.username} - {self.message[:30]}..."  
