from django.urls import path
from . import views

urlpatterns = [
    path('autores/', views.author_list, name='author-list'),
    path('livros/', views.book_list, name='book-list'),
    path('autores/top/', views.top_authors, name='top-authors'),

]
