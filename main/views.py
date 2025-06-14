from django.shortcuts import render
from .models import *


def index_view(request):
    return render(request,'index.html')


def all_proffesors_view(request):
    return render(request, 'all-professors.html')

def all_students_view(request):
    return render(request, 'all-students.html')

def add_professor_view(request):
    return render(request, 'add-professor.html')

def add_student_view(request):
    return render(request, 'add-student.html')

def edit_professor_view(request):
    return render(request, 'edit-professor.html')

def edit_student_view(request):
    return render(request, 'edit-student.html')

def professor_profile_view(request):
    return render(request, 'professor-profile.html')

def student_profile_view(request):
    return render(request, 'student-profile.html')

def all_courses_view(request):
    return render(request, 'all-courses.html')

def add_course_view(request):
    return render(request, 'add-course.html')

def edit_course_view(request):
    return render(request, 'edit-course.html')

def course_info_view(request):
    return render(request, 'course-info.html')

def course_payment_view(request):
    return render(request, 'course-payment.html')
