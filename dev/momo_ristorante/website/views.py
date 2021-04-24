from django.http import HttpResponse
from django.shortcuts import render
from momos.models import Momo
from blogs.models import Blog
from .models import Homepage, Setting

def datas():
    data = {
        "homepage": Homepage.objects.all(),
        "momos": Momo.objects.all(),
        "blogs" : Blog.objects.all(),
        "jumbotron": Homepage.objects.get(pk='jumbotron'),
        "setting": Setting.objects.get(pk=1),
    }
    return data

def home(request):
    if request.user.is_authenticated:
        return render(request, "website/index.html", datas())
    else:
        return HttpResponse('you are not authenticated!')

def reference(request):
    return render(request, 'references/reference.html', datas())  

def underconstruction(request):
    return render(request, 'under_construction/under_construction.html')

def booking(request):
    return render(request, 'website/booking.html')