from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
import requests


from rest_framework.renderers import JSONRenderer

from .forms import application_form
from .serializers import MyfileSerializer
from .models import Application


URL = 'https://recruitment.fisdev.com/api/v1/recruiting-entities/'


def post_application(request, i=None):
    data = Application.objects.all()[:1]
    print(data)
    serializer = MyfileSerializer(data)
    json_data = JSONRenderer().render(serializer.data)
    headers = {'Authorization': 'Token 289429d7163f866b36b937a99e2aa6365755ce69'}
    requests.post(url=URL, headers=headers, data=json_data)

    if i==1:
        i = 2
        request.post_application(request, i)
    return HttpResponse("Success")


@csrf_exempt
def application_data(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        full_address = request.POST['full_address']
        name_of_university = request.POST['name_of_university']
        graduation_year = request.POST['graduation_year']
        cgpa = request.POST['cgpa']
        experience_in_months = request.POST['experience_in_months']
        current_work_place_name = request.POST['current_work_place_name']
        applying_in = request.POST['applying_in']
        expected_salary = request.POST['expected_salary']
        field_buzz_reference = request.POST['field_buzz_reference']
        github_project_url = request.POST['github_project_url']
        cv_file = request.FILES['cv_file']


        application = Application.objects.create(name=name, email=email, phone=phone,
                                       full_address=full_address,name_of_university=name_of_university,
                                       graduation_year=graduation_year,
                                       cgpa=cgpa, experience_in_months=experience_in_months,
                                       current_work_place_name=current_work_place_name, applying_in=applying_in,
                                       expected_salary=expected_salary, field_buzz_reference=field_buzz_reference,
                                       github_project_url=github_project_url, cv_file=cv_file,
                                       )
        application.save()
        return redirect('post_application')
    else:
        value = application_form()
        return render(request, 'app1/application_form.html', {'value': value})
