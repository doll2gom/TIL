from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField(null=True)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=3)
    ceated_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True)
    # ceated_at = models.DateTimeField(auto_now_add=True)
    # 날짜와 시간까지 기록
    # deadline = models.DateField(null=True)
    # 날짜만 기록
    
