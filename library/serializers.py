from rest_framework import serializers
from library.models import Author,Book,Member,BorrowRecord

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name','biography']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Book
        fields =['id','title','author','isbn','category','availability_status']

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['user','membership_date']

class BorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = ['book','member','borrow_date','return_date']