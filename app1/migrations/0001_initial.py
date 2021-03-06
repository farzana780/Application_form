# Generated by Django 3.1.4 on 2020-12-19 11:31

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('tsync_id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Tsync_ID')),
                ('name', models.TextField(max_length=256)),
                ('email', models.EmailField(max_length=256)),
                ('phone', models.TextField(max_length=14)),
                ('full_address', models.TextField(max_length=512)),
                ('name_of_university', models.TextField(max_length=256)),
                ('graduation_year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2016), django.core.validators.MaxValueValidator(2020)])),
                ('cgpa', models.FloatField(validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(4)])),
                ('experience_in_months', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('current_work_place_name', models.TextField(max_length=256)),
                ('applying_in', models.CharField(choices=[('Mobile,', 'mobile'), ('Backend', 'backend')], default='', max_length=7)),
                ('expected_salary', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(15000), django.core.validators.MaxValueValidator(60000)])),
                ('field_buzz_reference', models.TextField(max_length=256)),
                ('github_project_url', models.URLField(max_length=512)),
                ('cv_file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
