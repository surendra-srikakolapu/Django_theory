from pyexpat import model
from django import forms
from .models import Employee


class EmployeeModelForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
