from typing import reveal_type

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def services(request):
    return render(request, 'service-details.html')
def starter(request):
    return render(request, 'starter-page.html')