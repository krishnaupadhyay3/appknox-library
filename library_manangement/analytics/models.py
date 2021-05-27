from django.db import models

# Create your models here.

class AuthorCategory(models.Model):
    class Meta:
        table_name="author"

class BookCategory(models.Model):
    class Meta:
        table_name="book"