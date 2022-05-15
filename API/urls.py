from django.urls import path
from API.views import *
from rest_framework.routers import DefaultRouter
from API.views import EmployeeViewSet
from API.views import data_format
from rest_framework.authtoken import views


router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')
urlpatterns = router.urls

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('data-format', data_format, name="data-format"),
    path('exportcsv', emp_export_csv, name="emp-csv-export"),
    path('exportxls', emp_export_excel, name="emp-excel-export"),
    path('upload-csv/', csv_upload, name="csv_upload"),
    path('importxls', emp_import_excel, name="emp-excel-import"),


    path('delete_emp/<int:id>/', delete_emp, name="delete-emp"),
    path('update_emp/<int:id>/', update_emp, name="update-emp"),
    path('emp_table', emp_table, name="emp-table"),
    path('del_table', del_table, name="del-table"),
]

urlpatterns += router.urls
