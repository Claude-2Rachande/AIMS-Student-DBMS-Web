from django.db import models
from django.core.exceptions import ValidationError
from students.models import Student
from courses.models import Course


class Enrollment(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.PROTECT
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT
    )

    enrollment_date = models.DateField(
        auto_now_add=True
    )

    class Meta:
        unique_together = (
            'student',
            'course',
        )

        ordering = [
            'student',
            'course',
        ]

    def clean(self):
        super().clean()

        if not self.course.programs.filter(
            pk=self.student.program.pk
        ).exists():
            raise ValidationError(
                "A student can only enroll in courses assigned to their program."
            )

        current_enrollments = Enrollment.objects.filter(
            course=self.course
        ).exclude(
            pk=self.pk
        ).count()

        if current_enrollments >= self.course.capacity:
            raise ValidationError(
                f"{self.course.course_code} has reached its maximum capacity "
                f"of {self.course.capacity} students."
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.student.registration_number}"
            f" -> "
            f"{self.course.course_code}"
        )