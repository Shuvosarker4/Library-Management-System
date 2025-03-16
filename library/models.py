from django.db import models
from users.models import User
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')
    isbn = models.CharField(max_length=15,unique=True)
    category = models.CharField(max_length=100)
    availability_status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Member(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='member')
    membership_date =models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name

class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrow_book")
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="borrow_member")
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.member.user.email} borrowed {self.book.title}"
