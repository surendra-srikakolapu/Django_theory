from django.contrib import admin
from .models import Class, Student


class StudentInLineAdmin(admin.TabularInline):
    model = Student


class ClassAdmin(admin.ModelAdmin):
    inlines = [StudentInLineAdmin]


admin.site.register(Class, ClassAdmin)
admin.site.register(Student)
