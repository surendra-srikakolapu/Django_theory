from django.shortcuts import render
from .models import *
from Accounts.models import *
from API.models import *
from books.models import *
from payment_gateway.models import Order


def Portfolio(request):

    users_count = User.objects.all().count()
    emps_count = Employee.objects.all().count()
    studs_count = Student.objects.all().count()
    payment_count = Order.objects.all().count()

    return render(request, 'Homepage/portfolio.html', {'users_count': users_count, 'studs_count': studs_count, 'emps_count': emps_count, 'payment_count': payment_count})


def Files(request):

    files = Upload_download_file.objects.all()

    return render(request, 'others/download_list.html', {'files': files})
