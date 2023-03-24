from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('todos', views.todo, name="todo"),
]
