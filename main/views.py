from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages 
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.conf import settings

def login_view(request):
    form = LoginForm(data=request.POST or None)
    errors = []

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # ✅ Sessiya muddati
            if not request.POST.get('remember_me'):
                request.session.set_expiry(0)
            else:
                request.session.set_expiry(60 * 60 * 24 * 30)

            # ✅ Superuser (admin) bo‘lsa admin panelga
            if user.is_superuser:
                return redirect('/')

            # ✅ Profile bor bo‘lsa — roli bo‘yicha yo‘naltirish
            if hasattr(user, 'profile'):
                role = user.profile.role
                if role == 'teacher':
                    return redirect('/teacher-dashboard/')
                elif role == 'student':
                    return redirect('/student-dashboard/')

            # 👤 Roli yo‘q bo‘lsa asosiy sahifaga
            return redirect('/')
        else:
            errors = form.errors.get('__all__', [])

    return render(request, 'register/login.html', {
        'login_form': form,
        'errors': errors
    })
    
def logout_view(request):
    logout(request)
    return redirect('/login/') 


def index_view(request):
    return render(request,'index.html')


def all_proffesors_view(request):
    query = request.GET.get('q')

    professors = ProfileUser.objects.filter(role='teacher', is_approved=True)

    if query:
        professors = professors.filter(
            Q(full_name__icontains=query) |
            Q(phone_number__icontains=query)
        )

    context = {
        'professors': professors
    }
    return render(request, 'all-professors.html', context)



def all_students_view(request):
    query = request.GET.get('q')

    students = ProfileUser.objects.filter(role='student', is_approved=True)

    if query:
        students = students.filter(
            Q(full_name__icontains=query) |
            Q(phone_number__icontains=query)
        )

    context = {
        'students': students
    }
    return render(request, 'all-students.html', context)



def all_courses_view(request):
    query = request.GET.get('q')
    
    if query:
        courses = add_course_model.objects.filter(
            Q(department__icontains=query) |
            Q(name__icontains=query)
        )
    else:
        courses = add_course_model.objects.all()
    
    context = {
        'courses': courses
    }
    return render(request, 'all-courses.html',context)



def add_professor_view(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.role = 'teacher'
            profile.is_approved = False  # ❗
            profile.save()
            messages.success(request, "O‘qituvchi so‘rovnomasi yuborildi. Tasdiq kutmoqda.")
            return redirect('/pending-requests/')
    else:
        form = ProfessorForm()
    return render(request, 'add-professor.html', {'form': form})



def add_student_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.role = 'student'
            profile.is_approved = False  # ❗
            profile.save()
            messages.success(request, "O‘quvchi so‘rovnomasi yuborildi. Tasdiq kutmoqda.")
            return redirect('/pending-requests/')
    else:
        form = StudentForm()
    return render(request, 'add-student.html', {'form': form})




def add_course_view(request):
    if request.method == 'POST':
        forms = CoursesForm(request.POST)

        if forms.is_valid():
            forms.save()
            messages.success(request,'Gruppa muvaffaqiyatli Yaratildi !!')
            return redirect('/all-courses/')
        else:
            messages.error(request,"Gruppa yaratilishda Xatolik Mavjud !! ")
    else:
        forms = CoursesForm()
    context={
        'forms':forms,
        'group':add_course_model.objects.all(),
    }
    return render(request, 'add-course.html',context)

def edit_professor_view(request, professor_id):
    professor = get_object_or_404(ProfileUser, id=professor_id, role='teacher')

    if request.method == 'POST':
        # faqat ProfileUser maydonlarini yangilaymiz, user ga tegmaymiz
        professor.full_name = request.POST.get('full_name')
        professor.address = request.POST.get('address')
        professor.phone_number = request.POST.get('phone_number')
        professor.birth_date = request.POST.get('birth_date')
        professor.description = request.POST.get('description')
        professor.department = request.POST.get('department')

        # ⚠️ user_id ni o‘zgartirmaymiz!
        professor.save()
        return redirect('/all-professors/')

    context = {
        'professor': professor
    }
    return render(request, 'edit-professor.html', context)


def delete_professor_view(request, professor_id):
    professor = get_object_or_404(ProfileUser, id=professor_id, role='teacher')
    professor.delete()
    return redirect('/all-professors/')


def delete_student_view(request, student_id):
    student = get_object_or_404(ProfileUser, id=student_id, role='student')
    student.delete()
    return redirect('/all-students/')

def edit_student_view(request, student_id):
    student = get_object_or_404(ProfileUser, id=student_id, role='student')
    groups = add_course_model.objects.all()

    if request.method == 'POST':
        student.full_name = request.POST.get('full_name')
        student.address = request.POST.get('address')
        student.phone_number = request.POST.get('phone_number')
        student.birth_date = request.POST.get('birth_date')
        student.description = request.POST.get('description')

        group_id = request.POST.get('group')
        if group_id:
            student.group_id = group_id

        student.save()
        return redirect('/all-students/')

    context = {
        'student': student,
        'groups': groups
    }
    return render(request, 'edit-student.html', context)


def edit_course_view(request, course_id):
    course = get_object_or_404(add_course_model, id=course_id)
    professors = ProfileUser.objects.filter(role='teacher')  # ✅ Faqat o‘qituvchilar

    if request.method == 'POST':
        course.name = request.POST.get('name')
        course.time = request.POST.get('time')
        course.course_price = request.POST.get('course_price')
        course.department = request.POST.get('department')
        course.description = request.POST.get('description')

        professor_id = request.POST.get('professor')
        if professor_id:
            course.professor_id = professor_id

        course.save()
        return redirect('/all-courses/')

    context = {
        'course': course,
        'professors': professors,
    }
    return render(request, 'edit-course.html', context)


def delete_course_view(request, course_id):
    course = get_object_or_404(add_course_model, id=course_id)
    course.delete()
    return redirect('/all-courses/')



#MANAGEMENT (TOP)

def mark_attendance(request, course_id):
    course = get_object_or_404(add_course_model, id=course_id)
    students = ProfileUser.objects.filter(role='student', group=course, is_approved=True)
    today = date.today()

    if request.method == 'POST':
        for student in students:
            status = request.POST.get(f'attend_{student.id}') == 'on'
            Attendance.objects.update_or_create(
                student=student,
                course=course,
                date=today,
                defaults={'status': status}
            )
        return redirect('/attendance-success/')

    return render(request, 'management/attendance.html', {
        'course': course,
        'students': students,
        'today': today
    })

    
def make_payment(request, student_id):
    student = get_object_or_404(ProfileUser, id=student_id, role='student', is_approved=True)
    course = student.group

    if request.method == 'POST':
        amount = request.POST['amount']
        month = request.POST['month']
        Payment.objects.update_or_create(
            student=student,
            course=course,
            month=month,
            defaults={'amount': amount, 'is_paid': True}
        )
        return redirect('/payment-success/')

    return render(request, 'management/make_payment.html', {
        'student': student
    })

    
def payment_success(request):
    return render(request, "management/payment-success.html")

def attendance_success(request):
    return render(request, "management/attendance-success.html")
    
def all_groups_view(request):
    groups = add_course_model.objects.all()
    return render(request, 'management/all_groups.html', {'groups': groups})

def students_in_group(request, course_id):
    course = get_object_or_404(add_course_model, id=course_id)
    students = ProfileUser.objects.filter(role='student', group=course, is_approved=True)
    return render(request, 'management/students_in_group.html', {
        'course': course,
        'students': students
    })
    
   
from calendar import monthrange   
    
def get_month_name(month):
    names = [
        "", "Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun",
        "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr"
    ]
    return names[month]

def attendance_journal(request, course_id, year, month):
    course = get_object_or_404(add_course_model, id=course_id)
    students = ProfileUser.objects.filter(role='student', group=course, is_approved=True)

    days_in_month = monthrange(year, month)[1]
    start_date = date(year, month, 1)
    end_date = date(year, month, days_in_month)
    date_list = [
        (date(year, month, day), date(year, month, day).isoformat())
        for day in range(1, days_in_month + 1)
    ]

    attendance_records = Attendance.objects.filter(
        course=course,
        date__range=(start_date, end_date)
    )
    attendance_dict = {
        f"{record.student_id}_{record.date.isoformat()}": record.status
        for record in attendance_records
    }

    month_str = f"{get_month_name(month)} {year}"
    payment_records = Payment.objects.filter(course=course, month=month_str)
    payment_dict = {
        record.student_id: record.is_paid for record in payment_records
    }

    context = {
        "course": course,
        "students": students,
        "date_list": date_list,
        "year": year,
        "month": month,
        "month_name": get_month_name(month),
        "attendance": attendance_dict,
        "payments": payment_dict,
    }

    return render(request, "management/attendance_journal.html", context)


def course_list_view(request):
    courses = add_course_model.objects.all()
    return render(request, 'management/courses.html', {'courses': courses})

def select_month_view(request, course_id):
    course = add_course_model.objects.get(id=course_id)
    return render(request, 'management/months.html', {'course': course})


def pending_requests_view(request):
    pending_users = ProfileUser.objects.filter(is_approved=False)
    return render(request, 'management/pending_users.html', {
        'pending_users': pending_users
    })

def approve_user_view(request, user_id):
    user = get_object_or_404(ProfileUser, id=user_id)
    user.is_approved = True
    user.save()
    return redirect('/pending-requests/')  # yoki boshqa sahifa

def reject_user_view(request, user_id):
    user = get_object_or_404(ProfileUser, id=user_id)
    user.user.delete()  # Asosiy User modelini o‘chiradi
    return redirect('/pending-requests/')


def send_notification_view(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        message_type = request.POST.get('message_type')

        student = get_object_or_404(ProfileUser, id=student_id, role='student')

        if message_type == "kelmagan":
            message = "📌 Bugungi darsga kelmadingiz."
        elif message_type == "tolov":
            message = "💳 Iltimos, bu oy uchun to‘lovni amalga oshiring."
        else:
            message = "Noma'lum xabar turi."

        Notification.objects.create(
            user=student.user,
            message=message
        )

        messages.success(request, f"✅ Xabar foydalanuvchisiga yuborildi.")

    students = ProfileUser.objects.filter(role='student', is_approved=True)
    return render(request, 'management/send_notification.html', {'students': students})



#MANAGEMENT (BOTTOM)

    
    

def Password_reset(request):
    return render(request,'password-recovery.html')



def student_dashboard_view(request):
    return render(request, "index-2.html")


@login_required
def student_profile_view(request):
    profile = get_object_or_404(ProfileUser, user=request.user, role='student')

    if request.method == 'POST':
        form = StudentEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("/student-dashboard/")
    else:
        form = StudentEditForm(instance=profile)

    return render(request, 'student/profile.html', {'form': form, 'profile': profile})

    
@login_required
def student_notifications_view(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'student/notifications.html', {'notifications': notifications})


@login_required
def mark_notification_read(request, notif_id):
    notif = get_object_or_404(Notification, id=notif_id, user=request.user)
    notif.is_read = True
    notif.save()
    return redirect('student_notifications')


@login_required
def delete_notification(request, notif_id):
    notif = get_object_or_404(Notification, id=notif_id, user=request.user)
    notif.delete()
    return redirect('student_notifications')


@login_required
def student_group_view(request):
    profile = get_object_or_404(ProfileUser, user=request.user, role='student', is_approved=True)

    if not profile.group:
        return render(request, 'student/no_group.html')  # Agar hali guruh biriktirilmagan bo‘lsa

    group = profile.group
    students = ProfileUser.objects.filter(group=group, role='student', is_approved=True)

    return render(request, 'student/group_detail.html', {
        'group': group,
        'students': students,
        'profile': profile
    })

from datetime import date, timedelta

from datetime import date, timedelta

@login_required
def student_attendance_view(request):
    student = get_object_or_404(ProfileUser, user=request.user, role='student')

    today = date.today()
    month_start = today.replace(day=1)
    if month_start.month == 12:
        next_month = month_start.replace(year=month_start.year + 1, month=1, day=1)
    else:
        next_month = month_start.replace(month=month_start.month + 1, day=1)

    days_in_month = (next_month - month_start).days

    date_list = []
    for day in range(1, days_in_month + 1):
        day_obj = month_start.replace(day=day)
        day_str = day_obj.strftime('%Y-%m-%d')
        date_list.append((day_obj, day_str))

    # 🔥 Faqat joriy oydagi davomatni olish
    attendance = {}
    attendance_qs = Attendance.objects.filter(
        student=student,
        date__gte=month_start,
        date__lt=next_month
    )
    for att in attendance_qs:
        key = f"{student.id}_{att.date.strftime('%Y-%m-%d')}"
        attendance[key] = True

    # 🔥 To‘lov ham shu oy uchun (ixtiyoriy)
    payments = {}
    payment_qs = Payment.objects.filter(
        student=student,
        payment_date__gte=month_start,
        payment_date__lt=next_month
    )
    if payment_qs.exists():
        payments[student.id] = True

    context = {
        'student': student,
        'attendance': attendance,
        'payments': payments,
        'date_list': date_list,
        'month_name': month_start.strftime('%B'),
        'year': today.year,
    }
    return render(request, 'student/attendance_journal.html', context)



def teacher_dashboard_view(request):
    return render(request, "index-1.html")

@login_required
def teacher_groups_view(request):
    profile = get_object_or_404(ProfileUser, user=request.user, role='teacher')
    groups = add_course_model.objects.filter(professor=profile)

    for group in groups:
        group.student_count = ProfileUser.objects.filter(group=group, role='student').count()

    return render(request, 'teacher/groups.html', {'groups': groups})


@login_required
def teacher_group_detail_view(request, group_id):
    group = get_object_or_404(add_course_model, id=group_id)
    students = ProfileUser.objects.filter(group=group, role='student', is_approved=True)

    return render(request, 'teacher/group_detail.html', {
        'group': group,
        'students': students
    })



