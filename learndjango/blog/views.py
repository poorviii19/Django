from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def home(request):
    return HttpResponse("<h1> Welcome to my Blog!</h1>")


def about(request):
    return HttpResponse("<h1> About Us:<h1> <p> This is django's blog</p>")

def current_time(request):
    now = datetime.datetime.now()
    html = f"<h1> current time is: {now} </h1>"
    return HttpResponse(html)

def greet_user(request):
    hour = datetime.datetime.now().hour
    if hour<12:
        message = "Good Morning"
    elif hour<18:
        message = "Good Afternoon"
    else:
        message = "Good Evening"
    return HttpResponse(f"<h1>{message}</h1>")


# HTTP REQUESTS:
def request_info(request):
    method = request.method     # 'GET', 'POST', etc.
    path = request.path         # '/blog/time/'
    get_params = request.GET    # query string params (?key=value)
    post_data = request.POST    # form data (only on POST)
    headers = request.headers   # request headers

    user_agent = request.META.get('HTTP_USER_AGENT')

    html = f"""
        <h2>Request Info</h2>
        <p>Method: {method}</p>
        <p>Path: {path}</p>
        <p>GET params: {dict(get_params)}</p>
    """
    return HttpResponse(html)

