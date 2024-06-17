from django.urls import path
from theme.views import register, login, contactform, about, categories, contact, success
from . import views

app_name = 'books_fbv_admin'

urlpatterns = [
  path('', views.book_list, name='book_list'),
  path('new/', views.book_create, name='book_new'),
  path('edit/<int:pk>/', views.book_update, name='book_edit'),
  path('delete/<int:pk>/', views.book_delete, name='book_delete'),
  path('book/<int:pk>/borrow/', views.book_borrow, name='book_borrow'),
  path('register', register ,name='register'),
  path('login', login , name='login'),
  path('contactus' , contactform , name='contactus'),
  path('about', about , name='about'),
  path('category', categories , name='categories'),
  path('contact', contact, name='contact'),
  path('success', success, name='success'),
]