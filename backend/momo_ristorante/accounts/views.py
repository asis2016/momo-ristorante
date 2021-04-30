"""
    accounts/views.py
    _________________
"""
from django.shortcuts import render


def login(request):
    """ Login page. """
    return render(request, 'accounts/login.html')
