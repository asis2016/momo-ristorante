from django.shortcuts import render
from momos.models import Momo
from blogs.models import Blog
from .models import Homepage, Setting

def home(request):
    return render(request, "website/home.html", {
        "momos": Momo.objects.all(),
        "blogs" : Blog.objects.all(),
        "featurette": Homepage.objects.get(pk='featurette'),
        "jumbotron": Homepage.objects.get(pk='jumbotron'),
        "setting": Setting.objects.get(pk=1)
        })

def underconstruction(request):
    return render(request, "website/under-construction.html")