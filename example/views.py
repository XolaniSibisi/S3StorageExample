from django.shortcuts import render, get_object_or_404, redirect
from .forms import CarForm
from django.contrib import messages
import requests
from django.http import HttpResponseRedirect, HttpResponse, HttpResponse

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Car added successfully!')
            return redirect('index')
    else:
        form = CarForm()
    return render(request, 'example/index.html', {'form': form})

