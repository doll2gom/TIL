from django.urls import path
from . import views

app_name = 'catch'
urlpatterns = [
    path('catch/', views.catch, name='catch'),
]