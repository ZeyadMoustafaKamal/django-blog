from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.auther.username} , {self.title}'

