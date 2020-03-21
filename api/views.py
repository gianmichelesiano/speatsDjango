from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from ordini.models import Ordine
import dateutil.parser
import json

def home(request):
    return HttpResponse('<h1>Speats admin works</h1>')

@csrf_exempt
@require_http_methods(["GET", "POST"])
def speatsOrder(request):

    responce = request.body

    str_responce = responce.decode("UTF-8")
    json_responce = json.loads(str_responce)
    orders = json_responce['orders']


    for order in orders:

        accepted_at = dateutil.parser.isoparse(order['accepted_at'])
        fulfill_at =  dateutil.parser.isoparse(order['fulfill_at'])
        restaurant_id = int(order['restaurant_id'])
        restaurant_name = str(order['restaurant_name'])
        client_id = int(order['client_id'])
        client_first_name = str(order['client_first_name'])
        client_last_name = str(order['client_last_name'])
        missed_reason = str(order['missed_reason'])
        
        total_price = None
        if order['total_price'] is not None:
            total_price = float(order['total_price'])

        sub_total_price = None
        if order['sub_total_price'] is not None:
            sub_total_price = float(order['sub_total_price'])

        payment = str(order['payment'])

        tax_value = None
        if order['tax_value'] is not None:
            tax_value = float(order['tax_value'])

        currency = str(order['currency'])
        _type = str(order['type'])
        status = str(order['status'])
        source = str(order['source'])
        persons = int(order['persons'])

        latitude = None
        if order['latitude'] is not None:
            latitude = float(order['latitude'])

        longitude = None
        if order['longitude'] is not None:
            longitude = float(order['longitude'])

        Ordine(
            accepted_at = accepted_at,
            fulfill_at = fulfill_at,
            restaurant_id = restaurant_id,
            restaurant_name = restaurant_name,
            client_id = client_id,
            client_first_name = client_first_name,
            client_last_name = client_last_name,
            missed_reason = missed_reason,
            total_price = total_price,
            sub_total_price = sub_total_price,
            payment = payment,
            tax_value = tax_value,
            currency = currency,
            type = _type,
            status = status,
            source = source,
            persons = persons,
            latitude = latitude,
            longitude = longitude
        ).save()

    return HttpResponse('success')