from rest_framework import serializers
from .models import Application


class MyfileSerializer(serializers.Serializer):
    class Meta:
        model = Application
        field = ['tsync_id', 'name', 'email', 'phone', 'full_address', 'name_of_university',
                 'graduation_year', 'cgpa', 'experience_in_months', 'current_work_place_name',
                 'applying_in', 'expected_salary', 'field_buzz_reference', 'github_project_url',
                 'cv_file']
