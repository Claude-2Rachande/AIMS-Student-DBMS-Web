from django.shortcuts import render, redirect, get_object_or_404
from .models import Program
from .forms import ProgramForm


def program_list(request):
    programs = Program.objects.all()
    return render(
        request,
        'programs/program_list.html',
        {
            'programs': programs
        }
    )


def add_program(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('program_list')
    else:
        form = ProgramForm()

    return render(
        request,
        'programs/program_form.html',
        {
            'form': form
        }
    )


def update_program(request, pk):
    program = get_object_or_404(Program, pk=pk)

    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            return redirect('program_list')
    else:
        form = ProgramForm(instance=program)

    return render(
        request,
        'programs/program_form.html',
        {
            'form': form
        }
    )
def delete_program(request, pk):

    program = get_object_or_404(
        Program,
        pk=pk
    )

    if request.method == 'POST':

        program.delete()

        return redirect(
            'program_list'
        )

    return render(
        request,
        'programs/program_confirm_delete.html',
        {
            'program': program
        }
    )