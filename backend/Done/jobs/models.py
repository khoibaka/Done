from django.db import models
from users.models import MyUser
# Create your models here.

class Job(models.Model):
    host = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    