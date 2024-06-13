from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from atexit import register
from theme.views import register, login, contactus, about, home, categories

# existing urlpatterns
urlpatterns = [
    path('', home, name='home'),
    path('books_fbv_admin/', include('books_fbv_admin.urls')),
    path('accounts/', include('django.contrib.auth.urls')),    
    path('admin/', admin.site.urls),
    path('register', register ,name='register'),
    path('login', login , name='login'),
    path('contactus' , contactus , name='contactus'),
    path('about', about , name='about'),
    path('category', categories , name='categories'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)