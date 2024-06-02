from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'pages', 'author', 'publisher', 'category', 'stock', 'cover_image']  # Updated fields

@login_required
def book_list(request, template_name='books_fbv_admin/book_list.html'):
    book = Book.objects.all()
    data = {}
    data['object_list'] = book
    return render(request, template_name, data)

@login_required
def book_borrow(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.stock > 0:
        book.stock -= 1
        book.save()
    return redirect('/')

@login_required
def book_create(request, template_name='books_fbv_admin/book_form.html'):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)  # Updated to handle file upload
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('books_fbv_admin:book_list')
    else:
        form = BookForm()
    return render(request, template_name, {'form':form})

@login_required
def book_update(request, pk, template_name='books_fbv_admin/book_form.html'):
    if request.user.is_superuser:
        book= get_object_or_404(Book, pk=pk)
    else:
        book= get_object_or_404(Book, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)  # Updated to handle file upload
        if form.is_valid():
            form.save()
            return redirect('books_fbv_admin:book_list')
    else:
        form = BookForm(instance=book)
    return render(request, template_name, {'form':form})

@login_required
def book_delete(request, pk, template_name='books_fbv_admin/book_confirm_delete.html'):
    if request.user.is_superuser:
        book= get_object_or_404(Book, pk=pk)
    else:
        book= get_object_or_404(Book, pk=pk, user=request.user)
    if request.method=='POST':
        book.delete()
        return redirect('books_fbv_admin:book_list')
    return render(request, template_name, {'object':book})
