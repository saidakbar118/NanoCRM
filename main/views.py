from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages 
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def register_view(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data['role']
            ProfileUser.objects.create(user=user, role=role)
            login(request, user)

            # Roli bo‘yicha sahifaga yuborish
            if role == 'teacher':
                return redirect('/add-professor/')
            elif role == 'student':
                return redirect('/add-student/')
            else:
                return redirect('/')

    return render(request, 'register/register.html', {'register_form': form})

from django.conf import settings

def login_view(request):
    form = LoginForm(data=request.POST or None)
    errors = []

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if not request.POST.get('remember_me'):
                request.session.set_expiry(0)
            else:
                request.session.set_expiry(60 * 60 * 24 * 30)

            if hasattr(user, 'profile') and user.profile.role:
                role = user.profile.role
                if role == 'teacher':
                    return redirect('/add-professor/')
                elif role == 'student':
                    return redirect('/add-student/')
            return redirect('/')
        else:
            # Xatoliklarni olish
            errors = form.errors.get('__all__', [])

    return render(request, 'register/login.html', {
        'login_form': form,
        'errors': errors
    })






@login_required
def choice_view(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        if role == 'teacher':
            return redirect('/')
        elif role == 'student':
            return redirect('/')
    return render(request, 'register/choice.html')


def teacher_register_view(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'register/teacher-register.html', {'form': form})

def student_register_view(request):
    form = ProfessorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'register/student-register.html', {'form': form})


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
