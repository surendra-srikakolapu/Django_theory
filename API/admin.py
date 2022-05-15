from pyexpat import model
from django.contrib import admin
from .models import Employee
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):

    list_display = ['name', 'dob', 'phone', 'company', 'address']

    class Meta:
        model = Employee


admin.site.register(Employee, EmployeeAdmin)
