
from django import forms
from .models import Application

class application_form(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('name', 'email', 'phone', 'full_address', 'name_of_university',
                 'graduation_year', 'cgpa', 'experience_in_months', 'current_work_place_name',
                 'applying_in', 'expected_salary', 'field_buzz_reference', 'github_project_url',
                 'cv_file')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'full_address': forms.TextInput(attrs={'class': 'form-control'}),
            'name_of_university': forms.TextInput(attrs={'class': 'form-control'}),
            'graduation_year': forms.NumberInput( attrs={'class': 'form-control'}),
            'cgpa': forms.NumberInput(attrs={'class': 'form-control'}),
            'experience_in_months': forms.NumberInput(attrs={'class': 'form-control'}),
            'current_work_place_name': forms.TextInput(attrs={'class': 'form-control'}),
            'applying_in': forms.Select(choices=[('Mobile,', 'mobile'), ('Backend', 'backend')], attrs={'class': 'form-control'}),
            'expected_salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'field_buzz_reference': forms.TextInput(attrs={'class': 'form-control'}),
            'github_project_url': forms.URLInput(attrs={'class': 'form-control'}),
            'cv_file': forms.FileInput(attrs={'class': 'form-control'}),

            # 'category': forms.Select(choices=cats, attrs={'class': 'form-control'}),
            # 'body': forms.Textarea(attrs={'class': 'form-control'}),
            # 'blog_image': forms.FileInput(attrs={'class': 'form-control'}),
        }