from django.shortcuts import render, redirect
from django.http import (HttpResponse, HttpResponseRedirect, JsonResponse,  Http404)
import datetime

# Create your views here.
# def home(request):
#     return HttpResponse("<h1> Welcome to my Blog!</h1>")


# def about(request):
#     return HttpResponse("<h1> About Us:<h1> <p> This is django's blog</p>")

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

def greet(request,name):
    return HttpResponse(f"the name is {name}")

def movieFinder(request, movie):
    
    movies = ['kgf', 'rrr', 'bahubali']

    if not movies:
        message = 'Please enter a movie name.'
    elif movie in movies:
        message = f'{movie.upper()} is available to watch.'
    else:
        message = f'Sorry ☹️, {movie.title()} was not found.'

    return HttpResponse(f'<h1>{message}</h1>')

def recipe(request):
    food = request.GET.get("food", "")
    if food:
        message = f"Recipe available for food = {food}"
    else:
        message = "Please enter a food name."
    return HttpResponse(message)


# Regular expression:
def userProfile(request, username):
    return HttpResponse(f"user profile is: {username}")


def productId(request, prod):
    return HttpResponse(f"product id is: {prod}")



# define its url in myproject
def handler404(request, exception):
    return HttpResponse(f"<h1>dear user the source you requested for is not found. {exception}</h1>")

def home(request):
    return render(request, 'blog/home.html')

# render() is a shortcut that combines: loading the template + filling in context data + returning an HttpResponse — all in one line.
def about(request):
    return render(request, 'blog/about.html')


# Creating request and response:
# Basic text/HTML response
def request_response(request):
    return HttpResponse("Learn the basics of http response with me")


# JSON response — very common for APIs
def json_response(request):
    data = {"name" : "Poorvi", "age" : "21", "city" : "phagwara"}
    return JsonResponse(data)

# Redirect response
def redirect_res(request):
    return HttpResponseRedirect('/blog/about/')

# Custom status code
def custom_res(request):
    return HttpResponse("Server is a teapot", status=418)

# shortcut of HttpResponseRedirect:
# This is preferred because if you ever change the URL path in urls.py, your redirect still works (since it references the name, not the literal string).
def redirecting(request):
    return redirect('home')

# Mapping URLs with Params
# You can capture parts of a URL as parameters using path converters.

def post_detail(request, post_id):
    return HttpResponse(f"<h1>Showing post #{post_id}</h1>")

def post_by_slug(request, slug):
    return HttpResponse(f"<h1>Post slug: {slug}</h1>")

def user_profile(request, username, year):
    return HttpResponse(f"<h1>{username}'s activity in {year}</h1>")


# practice:
def welcome(request):
    return HttpResponse("<h1>Blog Welcome page</h1>")

def post_details(request, post_id):
    posts = {1: "Intro to Django", 2: "Views and URLs"}
    if post_id not in posts:
        raise Http404("Post not found")
    return HttpResponse(f"<h1>{posts[post_id]}</h1>")

def api_data(request):
    return JsonResponse({"status": "ok", "framework": "Django"})

def old_home_redirect(request):
    return redirect('welcome')