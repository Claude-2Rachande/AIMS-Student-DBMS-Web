from django.db import models
from programs.models import Program
from django.core.exceptions import ValidationError
import re


def validate_registration_number(value):

    pattern = r"^AIMS\d{8}$"

    if not re.match(pattern, value):
        raise ValidationError(
            "Registration number must be in the format AIMS######## (AIMS followed by exactly 8 digits)."
        )


class Student(models.Model):

    registration_number = models.CharField(
        max_length=12,
        unique=True,
        validators=[validate_registration_number],
        help_text="Example: AIMS20260001 (AIMS + Cohort Year + Student Number)"
    )

    first_name = models.CharField(
        max_length=50
    )

    last_name = models.CharField(
        max_length=50
    )

    program = models.ForeignKey(
        Program,
        on_delete=models.PROTECT
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['registration_number']

    @property
    def cohort_year(self):
        return self.registration_number[4:8]

    def __str__(self):
        return (
            f"{self.registration_number} - "
            f"{self.first_name} {self.last_name}"
        )