from django.urls import path
from .views import *
urlpatterns=[
    path('',Index),
    path('all-professors/', all_proffesors),  
    path('all-students/', all_students),
    path('add-professor/', add_professor),
    path('add-student/', add_student),
    path('edit-professor/', edit_professor),
    path('edit-student/', edit_student),
    path('professor-profile/', professor_profile),
    path('student-profile/', student_profile),
]
