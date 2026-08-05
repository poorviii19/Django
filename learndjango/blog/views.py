from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1> Welcome to my Blog!</h1>")


def about(request):
    return HttpResponse("<h1> About Us:<h1> <p> This is django's blog</p>")