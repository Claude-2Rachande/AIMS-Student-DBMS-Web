from django.shortcuts import render, redirect, get_object_or_404
from .models import Enrollment
from .forms import EnrollmentForm


def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(
        request,
        'enrollments/enrollment_list.html',
        {
            'enrollments': enrollments
        }
    )


def add_enrollment(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm()

    return render(
        request,
        'enrollments/enrollment_form.html',
        {
            'form': form
        }
    )


def update_enrollment(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)

    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm(instance=enrollment)

    return render(
        request,
        'enrollments/enrollment_form.html',
        {
            'form': form
        }
    )


def delete_enrollment(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)

    if request.method == 'POST':
        enrollment.delete()
        return redirect('enrollment_list')

    return render(
        request,
        'enrollments/enrollment_confirm_delete.html',
        {
            'enrollment': enrollment
        }
    )