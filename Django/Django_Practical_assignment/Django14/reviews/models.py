from django.db import models
# from accounts.models import User
# from django.contrib.auth import get_user_model

## models.py에서 User를 참조할 때만 사용하는 방법이다.
from django.conf import settings

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = models.TextField(null=False)
    movie = models.CharField(max_length=80)
    hit = models.IntegerField(default=0, null=False)
    image = models.ImageField(upload_to='photo/', null=True, blank=True)


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(null=False)
