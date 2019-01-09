from django.http import HttpResponse
from django.shortcuts import render
# from django.contrib.auth.decorators import login_required # for future protection


# @login_required # for protecting specific locations
def welcome(request):
    """Send the user to home.html"""
    return render(request, 'generic/home.html', {'message': 'Can do!'})
