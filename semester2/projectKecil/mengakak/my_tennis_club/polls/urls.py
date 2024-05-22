from django.urls import path

from . import views

urlpatterns = [
    path('jawir/', views.jawir, name='hitamputih'),
]

urlpatterns = [
    path('', views.index, name='index'),
]
