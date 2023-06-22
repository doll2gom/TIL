from django.db import models
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80,blank=True)
    content = models.TextField(null=False,blank=True)
    category = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='posts/images/%Y/%m/%d/', null=True, blank=True)


# 이미지를 업로드 하고 제출 눌렀을 때
# 1 업로드한 이미지가 제출되지 않음
#  > 업로드한 이미지 사라짐
# 2 blank설정이 작동을 안한다