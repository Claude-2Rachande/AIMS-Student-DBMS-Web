from django import forms
from .models import Course


class CourseForm(forms.ModelForm):

    class Meta:

        model = Course

        fields = [
            'course_code',
            'course_name',
            'programs',
            'capacity'
        ]

        widgets = {
            'programs': forms.CheckboxSelectMultiple()
        }