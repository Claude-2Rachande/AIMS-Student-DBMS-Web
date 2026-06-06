from django.shortcuts import render
from programs.models import Program
from students.models import Student
from courses.models import Course
from enrollments.models import Enrollment


def dashboard(request):

    students = Student.objects.all()

    cohort_counts = {}

    for student in students:

        cohort = student.registration_number[4:8]

        cohort_counts[cohort] = (
            cohort_counts.get(cohort, 0) + 1
        )

    context = {

        'total_programs': Program.objects.count(),
        'total_students': Student.objects.count(),
        'total_courses': Course.objects.count(),
        'total_enrollments': Enrollment.objects.count(),

        'cohort_counts': cohort_counts

    }

    return render(
        request,
        'dashboard.html',
        context
    )