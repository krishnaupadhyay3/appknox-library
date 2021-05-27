from rest_framework import serializers
from .models import Author, Books, Categories
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = ('first_name', 'last_name','created_at')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }


    def create(self, validated_data):
        user = Author.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            created_at=validated_data['created_at']
        )

class BooksSerializer(serializers.ModelSerializer):
    isbn13 = serializers.CharField(
            required=True,
            validators=[UniqueValidator(queryset=Author.objects.all())]
            )
    class Meta:
        model = Books
        fields = ('book_name', 'published_date','authors','isbn13','category_name')
        extra_kwargs = {
            'book_name': {'required': True},
            'published_date': {'required': True},
            'authors': {'required': True},
            'isbn13': {'required': True},
            'category_name': {'required': True}
        }

    def create(self, validated_data):
        user = Books.objects.create(
            book_name=validated_data['first_name'],
             published_date=validated_data['published_date'],
             authors=validated_data['authors'],
             isbn13=validated_data['isbn13'],
             category_name= validated_data['category_name']
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('category_name')
        extra_kwargs = {
            'category_name': {'required': True}
        }
    def create(self, validated_data):
        user = Categories.objects.create(
             category_name= validated_data['category_name']
        )