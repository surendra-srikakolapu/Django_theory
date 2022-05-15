from django import forms
from django.forms.models import inlineformset_factory

from .models import Class, Student


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = "__all__"


class StudentForm(forms.ModelForm):

    stu_name = forms.CharField(label="", max_length="100", widget=forms.TextInput
                               (attrs={'placeholder': 'Enter Student Name'}))
    stu_age = forms.IntegerField(label="",  widget=forms.TextInput
                                 (attrs={'placeholder': 'Age'}))
    stu_fathername = forms.CharField(label="", max_length="50", widget=forms.TextInput
                                     (attrs={'placeholder': 'Enter Father Name'}))

    stu_address = forms.CharField(label="", max_length="150", widget=forms.TextInput
                                  (attrs={'placeholder': 'Enter Address'}))

    class Meta:
        model = Student
        fields = ('stu_name', 'stu_age', 'stu_fathername', 'stu_address')


StudentFormSet = inlineformset_factory(
    Class,
    Student,
    form=StudentForm,
    min_num=2,  # minimum number of forms that must be filled in
    extra=1,  # number of empty forms to display
    can_delete=False  # show a checkbox in each form to delete the row
)
