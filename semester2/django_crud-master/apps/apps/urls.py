from django.urls import include, path
from django.contrib import admin

import theme.views

urlpatterns = [
    path('', theme.views.home),
    path('books_fbv_admin/', include('books_fbv_admin.urls')),

    # Enable built-in authentication views
    path('accounts/', include('django.contrib.auth.urls')),    
    # Enable built-in admin interface
    path('admin/', admin.site.urls),
]
