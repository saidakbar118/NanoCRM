from django.urls import path
from .views import *
urlpatterns=[
    path('',index_view),
    path('all-professors/', all_proffesors_view), 
    # ustozlar 
    path('all-students/', all_students_view), 
    # student oquvchi
    path('add-professor/', add_professor_view),
    path('add-student/', add_student_view),
    path('edit-professor/', edit_professor_view),
    path('edit-student/', edit_student_view),
    path('professor-profile/', professor_profile_view),
    path('student-profile/', student_profile_view),
    path('add-course/', add_course_view),
    path('all-courses/', all_courses_view),
    # kurlas
    path('edit-course/', edit_course_view),
    path('course-info/',course_info_view),
    path('course-payment/',course_payment_view),
]
