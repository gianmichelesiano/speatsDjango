from django.db import models

# Create your models here.
class Ordine(models.Model):
    order_id = models.AutoField(primary_key=True)
    accepted_at = models.DateTimeField(blank=True, null=True)
    fulfill_at = models.DateTimeField(blank=True, null=True)
    restaurant_id = models.IntegerField(blank=True, null=True)
    restaurant_name = models.CharField(max_length=100,blank=True)
    client_id = models.IntegerField(blank=True, null=True)
    client_first_name = models.CharField(max_length=100,blank=True )
    client_last_name = models.CharField(max_length=100,blank=True)
    missed_reason = models.CharField(max_length=100,blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sub_total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment = models.CharField(max_length=100,blank=True)
    tax_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=100,blank=True)
    type = models.CharField(max_length=100,blank=True)
    status = models.CharField(max_length=100,blank=True)
    source = models.CharField(max_length=100,blank=True)
    persons = models.IntegerField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=15 , max_length=100, blank=True , null=True)



"""
          "missed_reason":null,
          "id":84430699,
          "total_price":14.45,
          "sub_total_price":14.45,
          "tax_value":0.35,
          "persons":0,
          "latitude":null,
          "longitude":null,
          "client_first_name":"Test",
          "client_last_name":"Test",
          "client_email":"test@gmail.com",
          "client_phone":"+41764466742",
          "restaurant_name":"Speats",
          "currency":"CHF",
          "type":"pickup",
          "status":"accepted",
          "source":"admin",
          "pin_skipped":false,   4t
          "accepted_at":"2020-03-18T17:03:38.000Z",
          "tax_type":"GROSS",
          "tax_name":"VAT",
          "fulfill_at":"2020-03-18T17:08:38.000Z",
          "reference":null,
"""
