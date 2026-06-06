from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        'course_code',
        'course_name',
        'get_programs',
        'capacity'
    )

    search_fields = (
        'course_code',
        'course_name'
    )

    def get_programs(self, obj):
        return ", ".join(
            [program.program_name for program in obj.programs.all()]
        )

    get_programs.short_description = "Programs"