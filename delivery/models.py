from django.db import models
from django_google_maps import fields as map_fields
from decimal import Decimal

class Consegne(models.Model):
    consegna_id = models.AutoField(primary_key=True)
    data_consegna = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=100,blank=True)
    indirizzo = models.CharField(max_length=100,blank=True)
    citta = models.CharField(
                    max_length=20,
                    choices=[
                        ('Schlieren', 'Schlieren'),
                        ('Urdorf', 'Urdorf'),
                        ('Dietikon', 'Dietikon'),
                        ('Zurigo', 'Zurigo'),
                    ],
                    default='Schlieren',
    ) 
    telefono   = models.CharField(max_length=100,blank=True)
    totale_ordine  = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    richiesta   = models.CharField(
                    max_length=20,
                    choices=[
                        ('telefono', 'telefono'),
                        ('eat.ch', 'eat.ch'),
                        ('uber', 'uber')
                    ],
                    default='Telefono',
    ) 

# Create your models here.

"""
data = { 'orderNumber': 101172259,
          'customerName' : 'Michele Carta',
          'customerAddress' : 'Brandstrasse 1, 8952 Schlieren',
          'customerEmail': '',
          'customerPhoneNumber': '',
          'restaurantName': 'La qualita',
          'restaurantAddress': 'Brandstrasse 37, 8952 Schlieren',
          'restaurantPhoneNumber': '0794466742',
          'orderItem':items,
          'totalOrderCost':'38.06',
          'tax':'0.0',
          'tips':'0.0',
          'deliveryFee':'0.0',
          'deliveryInstruction':'fast'};
"""