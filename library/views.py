from django.shortcuts import render
from rest_framework import viewsets
from library.models import Book,Author,BorrowRecord,Member
from library.serializers import BookSerializer,AuthorSerializer,BorrowRecordSerializer,MemberSerializer
from api.permissions import IsAdminOrReadOnly
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminOrReadOnly]

    @swagger_auto_schema(
        operation_summary='Retrive a list of Author'
    )
    def list(self, request, *args, **kwargs):
        """Retrive all the Author"""
        return super().list(request, *args, **kwargs)


class BookViewSet(viewsets.ModelViewSet):
    """
        API endpoint for managing books in the library
        - Allows authenticated admin to create, update, and delete books
    """
    permission_classes = [IsAdminOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @swagger_auto_schema(
        operation_summary='Retrive a list of Books'
    )
    def list(self, request, *args, **kwargs):
        """Retrive all the books"""
        return super().list(request, *args, **kwargs)

class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
    permission_classes = [IsAdminOrReadOnly]

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAdminOrReadOnly]