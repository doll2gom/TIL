from django.contrib import admin
# 명시적인 상대경로(모델이름)
# 현재 위치에서 models 모듈을 가져온다.
from .models import Todo
# from . import models

# Register your models here.
# "admin site"에 "register = 등록"하겠다..."Todo"모델을
@admin.register(Todo)

class 함수(admin.ModelAdmin):
    항목 = ['content', 'deadline', 'category']
    필터 = ['category']
    읭 = ['content']