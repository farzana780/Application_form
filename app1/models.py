import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Application(models.Model):
    tsync_id = models.UUIDField(auto_created=True,
                  primary_key = True,
                  serialize = False,
                  verbose_name ='Tsync_ID', max_length=55, default=uuid.uuid4, editable=False)

    name = models.TextField(max_length=256)
    email = models.EmailField(max_length=256)
    phone =models.TextField(max_length=14)
    full_address =models.TextField(max_length=512)
    name_of_university = models.TextField(max_length=256)
    graduation_year = models.PositiveIntegerField(validators=[MinValueValidator(2016), MaxValueValidator(2020)])
    cgpa = models.FloatField(validators=[MinValueValidator(2), MaxValueValidator(4)])
    experience_in_months = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    current_work_place_name = models.TextField(max_length=256)
    applying_in = models.CharField(max_length=7, choices=[('Backend', 'backend'),('Mobile,', 'mobile')], default='')
    expected_salary = models.PositiveIntegerField(validators=[MinValueValidator(15000), MaxValueValidator(60000)])
    field_buzz_reference = models.TextField(max_length=256)
    github_project_url = models.URLField(max_length=512)
    cv_file = models.FileField(blank=True, null=True, upload_to='file')


    class Meta:
        ordering = ['tsync_id']
