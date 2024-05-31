from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

import theme.views

# existing urlpatterns
urlpatterns = [
    path('', theme.views.home),
    path('books_fbv_admin/', include('books_fbv_admin.urls')),
    path('accounts/', include('django.contrib.auth.urls')),    
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)