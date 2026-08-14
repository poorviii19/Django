from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('time/', views.current_time, name = 'current_time'),
    path('greet/',views.greet_user, name = 'greet_user' ),
    path('info/', views.request_info, name='request_info'),
]