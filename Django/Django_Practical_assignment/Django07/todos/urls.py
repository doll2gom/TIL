from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('todos/', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('name/', views.get_name),

]