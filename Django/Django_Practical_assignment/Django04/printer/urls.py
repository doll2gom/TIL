from django.urls import path
from . import views

app_name = 'printer'
urlpatterns = [
    path('number-print/<int:num>', views.number_print, name='number'),
]