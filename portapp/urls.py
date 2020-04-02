from django.urls import path
from django.views.generic import TemplateView
from .views import about, contact, services

app_name = 'portapp'
urlpatterns = [

    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('services', services, name='services'),

]
