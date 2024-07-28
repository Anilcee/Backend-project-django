from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from accounts import views


urlpatterns = [
path('signupaccount/', views.signupaccount,
name='signupaccount'),
path('logout/', views.logoutaccount,
name='logoutaccount'),
path('login/', views.loginaccount,
name='loginaccount'),
]