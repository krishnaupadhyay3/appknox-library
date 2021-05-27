from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    class Meta :
        table_name = "author"

class Books(models.Model):
    book_name = models.CharField(max_length=200)
    published_date = models.DateTimeField()
    authors = models.CharField(max_length=500)
    isbn13  = models.IntegerField( unique=True) 
    category_name = models.CharField(max_length=200)
    class Meta :
        table_name = "book"

class Categories(models.Model):
    category_name = models.CharField(max_length=100)
    class Meta :
        table_name = "category"