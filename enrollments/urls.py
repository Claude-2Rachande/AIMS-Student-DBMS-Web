from django.urls import path
from .views import (
    enrollment_list,
    add_enrollment,
    update_enrollment,
    delete_enrollment,
)

urlpatterns = [
    path(
        '',
        enrollment_list,
        name='enrollment_list'
    ),
    path(
        'add/',
        add_enrollment,
        name='add_enrollment'
    ),
    path(
        'update/<int:pk>/',
        update_enrollment,
        name='update_enrollment'
    ),
    path(
        'delete/<int:pk>/',
        delete_enrollment,
        name='delete_enrollment'
    ),
]