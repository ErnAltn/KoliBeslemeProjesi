from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hakkinda(request):
    return render(request, 'anaSayfa/hakkinda.html')

def index(request):
    return render(request, 'anaSayfa/index.html')