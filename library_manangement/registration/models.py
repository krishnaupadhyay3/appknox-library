from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.TextField(null =False, unique=True)
    password = models.CharField(null=False, max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    user_name = models.CharField(max_length=30)