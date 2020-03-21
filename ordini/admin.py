from django.contrib.admin import ModelAdmin, register


from ordini.models import Ordine

@register(Ordine)
class OrdineAdmin(ModelAdmin):
    list_display = ('accepted_at', 'restaurant_name', 'client_first_name', 'client_last_name',  'payment', 'total_price')
