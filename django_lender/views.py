from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    """"""
    return render(request, 'generic/home.html', {'message': 'Can do!'})
    