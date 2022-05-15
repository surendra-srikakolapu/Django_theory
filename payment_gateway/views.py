from django.shortcuts import redirect, render
from .models import Order
from django.views.decorators.csrf import csrf_exempt
import razorpay
from Django_concepts.settings import (
    RAZORPAY_KEY_ID,
    RAZORPAY_KEY_SECRET,
)
from django.views.decorators.csrf import csrf_exempt


def Razorpay(request):
    return render(request, "razorpay.html")


def order_payment(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        client = razorpay.Client(
            auth=("rzp_test_PVhiCgaXFCMbOA", "SJNBeJnuta8mUBpfbO0CAAFe"))
        razorpay_order = client.order.create(
            {"amount": int(amount) * 100, "currency": "INR",
             "payment_capture": "1"}
        )
        order = Order.objects.create(
            name=name, amount=amount, provider_order_id=razorpay_order["id"]
        )
        order.save()
        return render(
            request,
            "payment.html",
            {
                "razorpay_key": RAZORPAY_KEY_ID,
                "order": order,
            },
        )

        return redirect('success')
    return render(request, "payment.html")


@csrf_exempt
def success(request):
    return render(request, "success.html")
