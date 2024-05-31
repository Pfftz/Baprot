# Generated by Django 5.0.6 on 2024-05-31 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_fbv_admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='Atmin Suki', max_length=200),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(default='All Categories', max_length=200),
        ),
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='covers/'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(default='ngawi industri', max_length=200),
        ),
    ]