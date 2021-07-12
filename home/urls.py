from django.urls import path
import home.views
app_name='home'

urlpatterns=[
path('', home.views.main, name='main'),
    path('home/',home.views.main,name='main'),
    ]