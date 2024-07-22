from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('signup', views.signup_view, name='signup'),
    path('userindex', views.userindex_views, name='userindex'),
    path('homepage', views.homepage_view, name='homepage'),
    path('logout', views.logout_action, name='logout'),
    path('rooms/<int:project_id>/', views.roomdetails_view, name='rooms'),
    path('createproject', views.createproject_view, name='createproject'),
    path('dashboard', views.dashboard_view, name= 'dashboard'),
]
