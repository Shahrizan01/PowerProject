from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('signup', views.signup_view, name='signup'),
    path('homepage', views.homepage_view, name= 'homepage'),
    path('logout', views.logout_view, name= 'logout'),
]
