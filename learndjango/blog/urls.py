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
    path('res/', views.request_response, name='request_response'),
    path('json/', views.json_response, name='json_response'),
    path('red/', views.redirect_res, name='redirect_res'),
    path('status/', views.custom_res, name='custom_res'),
    path('redirect/', views.redirecting, name='redirecting'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/', views.post_by_slug, name='post_by_slug'),
    path('user/<str:username>/<int:year>/', views.user_profile, name='user_profile'),



    re_path(r'^user/(?P<username>[a-zA-Z]+)/$' ,views.userProfile),
    re_path(r'^user/(?P<username>[a-zA-Z]*)/?$' ,views.userProfile),
    re_path(r'^product/(?P<prod>[a-zA-Z0-9]+)/$' ,views.productId),
]