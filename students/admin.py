from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        'registration_number',
        'first_name',
        'last_name',
        'get_cohort_year',
        'program'
    )

    search_fields = (
        'registration_number',
        'first_name',
        'last_name'
    )

    list_filter = (
        'program',
    )

    ordering = (
        'registration_number',
    )

    def get_cohort_year(self, obj):
        return obj.registration_number[4:8]

    get_cohort_year.short_description = 'Cohort'