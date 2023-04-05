from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    # path('new/', views.new, name='new'),
    path('articles/create/', views.create, name='create'),
    path('articles/<int:pk>/', views.detail, name='detail'),
    path('articles/<int:artilce_pk>/delete/', views.delete, name='delete'),
    # path('<int:article_pk>/edit/', views.edit, name='edit'),
    path('articles/<int:article_pk>/update/', views.update, name='update'),
]

