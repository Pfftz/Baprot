# Generated by Django 5.0.6 on 2024-05-31 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_fbv_admin', '0003_book_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, default='jempol.jpeg', upload_to=''),
        ),
    ]
