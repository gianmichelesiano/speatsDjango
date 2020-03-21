
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('speatsOrder/', views.speatsOrder, name='speatsOrder'), 
]
