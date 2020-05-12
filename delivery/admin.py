from django.contrib.admin import ModelAdmin, register
from django.conf import settings
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

import requests
import json


url = 'https://dispatch.questtag.com/Orders';
api_key = 'X60eTrW3Ir.jjs06XnYEqxdXsAtm7oo';

from delivery.models import Consegne

@register(Consegne)
class ConsegneAdmin(ModelAdmin):
    list_display = ('data_consegna', 'nome', 'indirizzo', 'citta', 'telefono' , 'totale_ordine' ,  'richiesta')

    def save_model(self, request, obj, form, change):
        itemList = []
        items = json.dumps(itemList)
        data = { 'orderNumber': 101172259,
                'customerName' : obj.nome,
                'customerAddress' : obj.indirizzo + ' ' + obj.citta,
                'customerEmail': '',
                'customerPhoneNumber': obj.telefono,
                'restaurantName': 'La qualita',
                'restaurantAddress': 'Brandstrasse 37, 8952 Schlieren',
                'restaurantPhoneNumber': '0794466742',
                'orderItem':items,
                'totalOrderCost': obj.totale_ordine,
                'tax':'0.0',
                'tips':'0.0',
                'deliveryFee':'0.0',
                'deliveryInstruction':'fast'}

        headers = {'Authorization': 'Basic '+api_key};       
        r = requests.post(url,data = data,headers = headers);
        reponse= r.json();    
        print(reponse);    
        obj.save()



