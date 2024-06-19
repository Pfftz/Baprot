from django.shortcuts import render,redirect
from books_fbv_admin.models import Book  # assuming you have a Book model in your models.py
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from theme.forms import ContactForm
from django.conf import settings
import logging
logger = logging.getLogger(__name__)
# Create your views here.

def home(request):
    books = Book.objects.all()
    return render(request, "home.html", {'books': books})

def categories(request):
    categories = ['Non Fiction', 'Fiction', 'Academy']
    books = {category: Book.objects.filter(category=category) for category in categories}
    return render(request, "category.html", {'books': books})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            html = render_to_string('emailTemplates.html', {'name': name, 'email': email, 'phone': phone, 'message': message})
            try:
                send_mail('The contact form subject', message, email, [settings.CONTACT_EMAIL], html_message=html)
            except Exception as e:
                logger.error("Failed to send email. Error: %s", e)
                messages.error(request, 'Failed to send email. Please try again later.')
                return render(request, 'contactus.html', {'form': form})
            return redirect('success')
        else:
            logger.error("Form is not valid. Errors: %s", form.errors)
    else:
        form = ContactForm()
    return render(request, 'contactus.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def contactform(request):
    return render(request,'contactus.html')

def about(request):
    return render(request,'about.html')

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