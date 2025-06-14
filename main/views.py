from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages 


def index_view(request):
    return render(request,'index.html')


def all_proffesors_view(request):
    return render(request, 'all-professors.html')

def all_students_view(request):
    return render(request, 'all-students.html')

def add_professor_view(request):
    if request.method == 'POST':
        forms = ProfessorForm(request.POST)

        if forms.is_valid():
            profile = forms.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('/add-professor/')
        else:
            messages.error(request,"Hisob yaratilishda Xatolik Mavjud !! ")
    else:
        forms = ProfessorForm()
    context={
        'forms':forms,
    }
    return render(request, 'add-professor.html',context)

def add_student_view(request):
    if request.method == 'POST':
        forms = StudentForm(request.POST)

        if forms.is_valid():
            profile = forms.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('/add-student/')
        else:
            messages.error(request,"Hisob yaratilishda Xatolik Mavjud !! ")
    else:
        forms = StudentForm()
    context={
        'forms':forms,
    }
    return render(request, 'add-student.html', context)

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
    if request.method == 'POST':
        forms = CoursesForm(request.POST)

        if forms.is_valid():
            forms.save()
            messages.success(request,'Gruppa muvaffaqiyatli Yaratildi !!')
            return redirect('/add-course/')
        else:
            messages.error(request,"Gruppa yaratilishda Xatolik Mavjud !! ")
    else:
        forms = CoursesForm()
    context={
        'forms':forms,
        'group':add_course_model.objects.all(),
    }
    return render(request, 'add-course.html',context)

def edit_course_view(request):
    return render(request, 'edit-course.html')

def course_info_view(request):
    return render(request, 'course-info.html')

def course_payment_view(request):
    return render(request, 'course-payment.html')
