from django.shortcuts import render
from books_fbv_admin.models import Book  # assuming you have a Book model in your models.py

def home(request):
    book = Book.objects.all()  # get all books
    return render(request, "home.html", {'object_list': book})