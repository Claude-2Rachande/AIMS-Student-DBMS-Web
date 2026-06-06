from django.db import models


class Program(models.Model):

    program_name = models.CharField(
        max_length=100
    )

    specialization = models.CharField(
        max_length=100
    )

    duration_months = models.PositiveIntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ['program_name']

        unique_together = (
            'program_name',
            'specialization'
        )

    def __str__(self):

        return (
            f"{self.program_name} "
            f"({self.specialization})"
        )