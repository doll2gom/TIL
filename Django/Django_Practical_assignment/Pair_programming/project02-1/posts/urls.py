from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    # path converters : URL변수타입 지정
    path('<int:post_pk>/',views.detail,name='detail'),
    path('<int:post_pk>/update/',views.update,name='update'),
    path('<int:post_pk>/delete/',views.delete,name='delete'),
    path('category/<str:subject>', views.category, name="category"),
]
