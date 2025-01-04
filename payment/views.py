import requests
import json

from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.conf import settings

from orders.models import Order


def payment_process(request):
    # Get Order Id From Session
    order_id = request.session.get('order_id')
    # Get Order Object
    order = get_object_or_404(Order, id=order_id)
    # Get Total Price Of Order By get_total_price() Class Method
    toman_total_price = order.get_total_price()
    # Convert Toman TO Rial For ZARINPAL Online Payment
    rial_total_price = toman_total_price * 10

    zarinpal_request_url = 'https://payment.zarinpal.com/pg/v4/payment/request.json'

    request_header = {
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    request_data = {
        'merchant_id': settings.MERCHANT_ID,
        'amount': rial_total_price,
        'description': f'{order_id}: first_name:{order.first_name} last_name:{order.last_name} email:{request.user.email}',
        'callback_url': 'http://127.0.0.1:8000',
        'email': request.user.email,
        'order_id': order_id,
    }

    res = requests.post(url=zarinpal_request_url, data=json.dumps(request_data), headers=request_header)
    data = res.json()['data']
    authority = data['authority']
    order.zarinpal_authority = authority
    order.save()

    if 'errors' not in data or len(data['errors'] == 0):
        return redirect('https://payment.zarinpal.com/pg/StartPay/{authority}'.format(authority=authority))
    else:
        return HttpResponse(f'Error From Zarinpal: {data["errors"].json()}')
