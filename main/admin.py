from django.contrib import admin
from .models import *

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


admin.site.register(add_professor_model)
admin.site.register(add_course_model)
admin.site.register(add_student_model)
