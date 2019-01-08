from django.db import models

class Book(models.Model):
    """This is the book class for the application"""
    title = models.CharField(max_length=48, default='')
    detail = models.CharField(max_length=4096, default='')
    author = models.CharField(max_length=255, default='')
    date_added = models.DateTimeField(auto_now_add=True)
    last_borrowed = models.DateTimeField(auto_now=True)


    STATES = [
        ('available', 'Available'),
        ('out', 'Checked Out')
    ]

    YEAR = [(str(i), str(i)) for i in range(1850, 2019)]

    status = models.CharField(max_length=48, default ='available', choices=STATES)
    year = models.CharField(choices=YEAR, max_length=4, default=1900)


    # def __repr__(self):
    #     return ''

    def __str__(self):
        return f'Book: {self.title} ({self.status})'

    