from django.urls import path
from . import views

urlpatterns = [

    path("", views.Razorpay, name="razorpay"),
    path("payment/", views.order_payment, name="payment"),
    path("success/", views.success, name="success"),
]
