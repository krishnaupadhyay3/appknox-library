from typing import cast
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import  generics
from .models import Author, Books , Categories
from .serializers import AuthorSerializer , BooksSerializer , CategorySerializer

class AuthorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AuthorSerializer

class BookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BooksSerializer

class CategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer