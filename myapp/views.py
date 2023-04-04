from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')
def games(request):
    return render(request, 'games.html')
def wakfu(request):
    return render(request, 'wakfu.html')
