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
    path('dashboard', views.dashboard_view, name='dashboard'),
    path('project', views.existproject_view, name='project'),
    path('projectdetails/<int:project_id>/', views.projectdetails_view, name='projectdetails'),
    path('movetorooms/<int:project_id>/', views.movetorooms_view, name='movetorooms'),
    path('delete/<int:project_id>/', views.deleteproject_view, name='delete'),
    path('editrooms/<int:project_id>/', views.editrooms_view, name='editrooms'),
    path('delete_room/<int:room_id>/', views.deleteroom_view, name='delete_room'),
]
