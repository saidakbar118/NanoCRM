from django.shortcuts import render
from .models import *


def Index(request):
    return render(request,'index.html')


def all_proffesors(request):
    return render(request, 'all-professors.html')

def all_students(request):
    return render(request, 'all-students.html')

def add_professor(request):
    return render(request, 'add-professor.html')

def add_student(request):
    return render(request, 'add-student.html')

def edit_professor(request):
    return render(request, 'edit-professor.html')

def edit_student(request):
    return render(request, 'edit-student.html')

def professor_profile(request):
    return render(request, 'professor-profile.html')

def student_profile(request):
    return render(request, 'student-profile.html')
