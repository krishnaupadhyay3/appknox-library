from .views import AuthorView , BookView ,CategoryView

from django.urls import path 
urlpatterns = [

    path('api/author/', AuthorView.as_view() ,name='author_create_update_delete'),
    path('api/book/', BookView.as_view(), name='books create_delete_update'),
    path('api/category/',CategoryView.as_view(), name="category create_update_delete"),


]