from django.contrib import admin
from django.urls import path
import account.views

app_name='account'

urlpatterns = [
    path('signup/',account.views.signup,name='signup'),
    path('signup_complete',account.views.signup_complete,name='signup_complete'),
    path('login/',account.views.login,name='login'),
    path('logout/',account.views.logout,name='logout'),
    path('login_or_signup/',account.views.login_or_signup,name='login_or_signup'),
]