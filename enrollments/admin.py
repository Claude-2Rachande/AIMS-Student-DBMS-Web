from django.contrib import admin
from .models import Enrollment


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):

    list_display = (
        'student',
        'course',
        'enrollment_date'
    )

    search_fields = (
        'student__registration_number',
        'course__course_code'
    )

    list_filter = (
        'course',
        'enrollment_date'
    )

    ordering = (
        '-enrollment_date',
    )