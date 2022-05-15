from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .models import Employee, ExcelFile
from .serializers import EmployeeSerializer
from .forms import EmployeeModelForm

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

import csv
import io
from django.contrib import messages

import requests
import pandas as pd
import csv


def data_format(request):

    return render(request, 'API/data_format.html')


class EmployeeViewSet(viewsets.ModelViewSet):

    authentication_classes = [SessionAuthentication,
                              BasicAuthentication, TokenAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


def emp_export_csv(request):
    employees = Employee.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=Employees.csv'
    writer = csv.writer(response)
    writer.writerow(['Employee Name', 'Date of Birth',
                    'Phone', 'Company', 'Address'])
    emps = employees.values_list(
        'name', 'dob', 'phone', 'company', 'address')
    for emp in emps:
        writer.writerow(emp)
    return response


def csv_upload(request):

    template = "API/csv_upload.html"
    data = Employee.objects.all()

    prompt = {
        'order': 'Order of the CSV should be image_name, objects_detected, timestamp',
        'csv_datas': data
    }

    if request.method == "GET":

        return render(request, template, prompt)

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
        return redirect('emp_table')

    data_set = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(data_set)

    next(io_string)
    for column in csv.reader(io_string):
        created = Employee.objects.update_or_create(
            name=column[0], dob=column[1], phone=column[2], company=column[3], address=column[4])

    context = {}
    return render(request, template, context)


def emp_export_excel(request):
    emps = Employee.objects.all()
    data = []

    for emp in emps:
        data.append({
            'Employee Name': emp.name,
            'Date of Birth': emp.dob,
            'Phone': emp.phone,
            'Company': emp.company,
            'Address': emp.address
        })

    pd.DataFrame(data).to_excel('Employee.xlsx')
    return JsonResponse({
        'status': 200
    })


def emp_import_excel(request):
    if request.method == "POST":
        file = request.FILES['files']

        emp = ExcelFile.objects.create(
            file=file
        )

        path = str(emp.file)

        print(f'{settings.BASE_DIR}/{path}')

        df = pd.read_excel(path)

        for d in df.values:
            print(d)

    return render(request, 'API/emp_excel_import.html')


def emp_table(request):

    if request.method == "POST":

        form = EmployeeModelForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('emp-table')

    else:

        form = EmployeeModelForm()
        emps = Employee.objects.all().order_by("name")

        from django.db.models import Q

        search = request.GET.get('search', '')
        if search:

            emps = emps.filter(Q(name__icontains=search) | Q(dob__icontains=search) | Q(
                phone__icontains=search) | Q(company__icontains=search) | Q(address__icontains=search))
    return render(request, 'API/employee_table.html', {'emps': emps, 'form': form})


def update_emp(request, id):

    emp = Employee.objects.get(id=id)
    uform = EmployeeModelForm(instance=emp)

    dict = {'uform': uform}

    if request.method == "POST":
        uform = EmployeeModelForm(request.POST, instance=emp)
        if uform.is_valid():
            uform.save()
            return redirect('emp-table')

    return render(request, 'API/employee_table.html', dict)


def delete_emp(request, id):

    emp = Employee.objects.get(id=id)
    emp.delete()
    messages.error(request, 'employee deleted')
    return redirect('emp-table')


def del_table(request):

    emps = Employee.objects.all()
    emps.delete()

    return redirect('emp-table')
