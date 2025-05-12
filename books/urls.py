from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('search/', views.search_books, name='search'),
    path('add/', views.add_book, name='add_book'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('category/<str:category>/', views.book_category, name='book_category'),
]
