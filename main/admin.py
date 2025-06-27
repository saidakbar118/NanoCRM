from django.contrib import admin
from .models import *

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


admin.site.register(add_course_model)
admin.site.register(Attendance)
admin.site.register(Payment)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('user__username', 'message')