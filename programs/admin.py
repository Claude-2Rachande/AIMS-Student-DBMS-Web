from django.contrib import admin
from .models import Program


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):

    list_display = (
        'program_name',
        'specialization',
        'duration_months'
    )

    search_fields = (
        'program_name',
        'specialization'
    )

    list_filter = (
        'specialization',
    )

    ordering = (
        'program_name',
    )