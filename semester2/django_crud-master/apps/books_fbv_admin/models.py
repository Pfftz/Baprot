from django.db import models
from django.urls import reverse
from django.conf import settings

class Book(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    pages = models.IntegerField()
    author = models.CharField(max_length=200, default="Atmin Suki")  # New field for author with default value
    publisher = models.CharField(max_length=200, default="ngawi industri")  # New field for publisher
    category = models.CharField(max_length=200, default="All Categories")  # New field for category
    stock = models.IntegerField(default=0)  # New field for stock with default value
    cover_image = models.ImageField(upload_to='covers', blank=True)  # New field for cover image

    def __str__(self):
        return str(self.name)  # Convert name to string representation

    def get_absolute_url(self):
        return reverse('books_fbv_admin:book_edit', kwargs={'pk': self.pk})