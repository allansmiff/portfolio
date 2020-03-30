from django.urls import path
from .views import index, about, contact, services

urlpatterns = [

    path('', index, name='inicio'),
    path('index.html', index),
    path('about.html', about, name='sobre'),
    path('contact.html', contact, name='contato'),
    path('services.html', services, name='serviços'),

]
