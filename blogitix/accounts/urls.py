from django.contrib.auth import views as auth_views # This line allows us to use the built-in Django authentication views and templates so that we don't have to write our own views and templates for login, logout, password reset, etc.
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('profile/', views.profile, name='profile'),
]
