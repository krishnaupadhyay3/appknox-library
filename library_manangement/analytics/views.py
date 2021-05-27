from django.shortcuts import render
from rest_framework import generics
from .models import AuthorCategory,BookCategory
# Create your views here.


class AuthorCategoryList(generics.GenericAPIView):
    def get_queryset(self):
        pk = self.request.pk
        count = AuthorCategory.objects.filter(category_name__contains=pk).count()
        return {"authors":count}

class BooksCategoryList(generics.GenericAPIView):
    def get_queryset(self):
        pk = self.request.pk
        count = BookCategory.objects.filter(category_name__contains=pk).count()
        return {"books":count}