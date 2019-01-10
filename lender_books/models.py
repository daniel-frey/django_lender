from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    """This is the book class for the application"""
    cover_image = models.ImageField(upload_to='media')
    title = models.CharField(max_length=48, default='')
    detail = models.CharField(max_length=4096, default='')
    author = models.CharField(max_length=255, default='')
    date_added = models.DateTimeField(auto_now_add=True)
    last_borrowed = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')

    STATES = [
        ('available', 'Available'),
        ('out', 'Checked Out')
    ]

    YEAR = [(str(i), str(i)) for i in range(1850, 2019)]

    status = models.CharField(max_length=48, default ='available', choices=STATES)
    year = models.CharField(choices=YEAR, max_length=4, default=1900)


    def __repr__(self):
        return f'<Book: {self.title}>'

    def __str__(self):
        return f'Book: {self.title} ({self.status})'
