from django.urls import path
from .views import (
    program_list,
    add_program,
    update_program,
    delete_program,
)

urlpatterns = [
    path(
        '',
        program_list,
        name='program_list'
    ),
    path(
        'add/',
        add_program,
        name='add_program'
    ),
    path(
        'update/<int:pk>/',
        update_program,
        name='update_program'
    ),
    path(
        'delete/<int:pk>/',
        delete_program,
        name='delete_program'
    ),
]