from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

@api_view(['GET', 'POST'])
def author_list(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        books = Book.objects.all()

        if search:
            books = books.filter(title__icontains=search)

        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.db.models import Count

@api_view(['GET'])
def top_authors(request):
    authors = Author.objects.annotate(book_count=Count('books')).order_by('-book_count')[:5]
    data = [
        {
            'id': author.id,
            'name': author.name,
            'book_count': author.book_count
        }
        for author in authors
    ]
    return Response(data)
