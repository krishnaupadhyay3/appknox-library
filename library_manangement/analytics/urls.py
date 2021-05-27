from .views import AuthorCategory,BooksCategoryList

from django.urls import path 
urlpatterns = [

    path('api/author/',  AuthorCategory.as_view() ,name='author_category_analytics'),
    path('api/book/', BooksCategoryList.as_view(), name='books_category_ananlytics'),

]