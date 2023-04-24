from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Album(models.Model):
    content = models.TextField(max_length=20)
    image = models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return f'[{self.pk}]{self.title} :: {self.author}'