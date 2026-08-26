from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('time/', views.current_time, name = 'current_time'),
    path('greet/',views.greet_user, name = 'greet_user' ),
    path('info/', views.request_info, name='request_info'),
    path('greet/<int:name>/', views.greet),
    path('movieFinder/<str:movie>/', views.movieFinder),
    path('recipe/', views.recipe, name='recipe'),
    # re_path(r'^user/(?P<username>[a-zA-Z]+)/$' ,views.userProfile),
    re_path(r'^user/(?P<username>[a-zA-Z]*)/?$' ,views.userProfile),
]