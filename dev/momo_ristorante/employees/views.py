from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import EmployeeForm


def index(request):
    return HttpResponse('from employee view')


def create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm()
    return render(request, 'employees/form.html', {'form': form})
