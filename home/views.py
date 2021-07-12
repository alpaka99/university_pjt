from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.conf import settings
from django.shortcuts import redirect

from django.contrib.auth.models import User
from account import views

# Create your views here.
def main(request):
    if request.user.is_authenticated:
        return render(request,'home/main.html')
    else:
        return render(request,'home/main.html')