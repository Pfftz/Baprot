from django.shortcuts import render,redirect
from books_fbv_admin.models import Book  # assuming you have a Book model in your models.py
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.mail import send_mail
from theme.forms import ContactModelForm

# Create your views here.

def home(request):
    books = Book.objects.all()
    return render(request, "home.html", {'books': books})

def categories(request):
    categories = ['Non Fiction', 'Fiction', 'Academy']
    books = {category: Book.objects.filter(category=category) for category in categories}
    return render(request, "category.html", {'books': books})

def contactus_email(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            contact = form.save()  # Save the form data to the database

            # send an email to yourself
            send_mail(
                'Contact Form Submission from {}'.format(contact.name),
                'Message: {}\nFrom: {}\nPhone: {}'.format(contact.message, contact.email, contact.phone),  # Include phone in the email
                contact.email,
                ['3337230041@untirta.ac.id'],  # replace with your email
            )
            return redirect('success')
    else:
        form = ContactModelForm()
    return render(request, 'contactus.html', {'form': form})

def index(request):
    return render(request , 'index.html')

def contactus(request):
    return render(request,'contactus.html')

def about(request):
    return render(request,'about.html')

def reaction(request):
    return render(request,'reaction.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
    
        if password==password2:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save();
            return redirect('login')
        else:
            messages.info(request,'password are not the same')
            return redirect('register')
    else:
        return render(request , 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username , password=password)

        if user is not None :
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials invalid')
            return redirect('login')
    else:
        return render(request,'login.html')