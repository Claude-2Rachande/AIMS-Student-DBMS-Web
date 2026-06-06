from django.db import models
from programs.models import Program
from django.core.exceptions import ValidationError
import re


def validate_course_code(value):
    pattern = r"^[A-Z]{2,5}\d{3,4}$"

    if not re.match(pattern, value):
        raise ValidationError(
            "Course code must be in a format like EPI701, STAT701 or DS701."
        )


class Course(models.Model):
    course_code = models.CharField(
        max_length=20,
        unique=True,
        validators=[validate_course_code]
    )

    course_name = models.CharField(
        max_length=100
    )

    programs = models.ManyToManyField(
        Program,
        related_name='courses',
        blank=True
    )

    capacity = models.PositiveIntegerField(
        default=30,
        help_text="Maximum number of students allowed in this course."
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['course_code']

    def delete(self, *args, **kwargs):
        if self.enrollment_set.exists():
            from django.core.exceptions import ProtectedError
            raise ProtectedError(
                f"Cannot delete course '{self.course_name}' "
                f"because it has active enrollments.",
                self.enrollment_set.all()
            )
        super().delete(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.course_code} - "
            f"{self.course_name}"
        )