from django.urls import path
from .views import *
urlpatterns=[
    path('',index_view),
    path('login/',login_view),
    path('logout/', logout_view, name='logout'),
    path('all-professors/', all_proffesors_view), 
    # ustozlar 
    path('all-students/', all_students_view), 
    # student oquvchi
    path('add-professor/', add_professor_view),
    path('add-student/', add_student_view),
    path('edit-professor/', edit_professor_view),
    path('edit-student/', edit_student_view),
    path('student-profile/', student_profile_view),
    path('add-course/', add_course_view),
    path('all-courses/', all_courses_view),
    # kurlas
    path('edit-course/', edit_course_view),
    path('attendance/<int:course_id>/', mark_attendance, name='mark_attendance'),
    path('payment/<int:student_id>/', make_payment, name='make_payment'),
    path('groups/', all_groups_view, name='all_groups'),
    path('group/<int:course_id>/students/', students_in_group, name='students_in_group'),
    path('journal/<int:course_id>/<int:year>/<int:month>/', attendance_journal, name='attendance_journal'),
    path('courses/', course_list_view, name='course_list'),
    path('course/<int:course_id>/months/', select_month_view, name='select_month'),
    path('payment-success/',payment_success),
    path('attendance-success/',attendance_success),

    #actions
    path('students/delete/<int:student_id>/', delete_student_view, name='delete_student'),
    path('students/edit/<int:student_id>/', edit_student_view, name='edit_student'),
    path('professors/delete/<int:professor_id>/', delete_professor_view, name='delete_professor'),
    path('professors/edit/<int:professor_id>/', edit_professor_view, name='edit_professor'),
    path('courses/delete/<int:course_id>/', delete_course_view, name='delete_course'),
    path('courses/edit/<int:course_id>/', edit_course_view, name='edit_course'),
    path('pending-requests/', pending_requests_view, name='pending_requests'),
    path('approve-user/<int:user_id>/', approve_user_view, name='approve_user'),
    path('reject-user/<int:user_id>/', reject_user_view, name='reject_user'),
    path('send-notification/', send_notification_view),
    
    # password reset
    path('password_reset/',Password_reset),
    
    #student
    path('student-dashboard/',student_dashboard_view),
    path('student/profile/', student_profile_view, name='student_profile'),
    path('student/notifications/', student_notifications_view, name='student_notifications'),
    path('student/notifications/<int:notif_id>/read/', mark_notification_read, name='mark_notification_read'),
    path('student/notifications/<int:notif_id>/delete/', delete_notification, name='delete_notification'),
    path('student/group/', student_group_view, name='student-group'),
    path('student/attendance/', student_attendance_view, name='student_attendance'),
    
    #teacher
    path('teacher-dashboard/',teacher_dashboard_view),
    path('teacher/groups/', teacher_groups_view, name='teacher_groups'),
    path('teacher/groups/<int:group_id>/', teacher_group_detail_view, name='teacher_group_detail'),
]
