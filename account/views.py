from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.db import IntegrityError
from account.models import Profile
#회원가입 함수
def login_or_signup(request):
    return render(request, "account/login_or_signup.html")

def signup(request):
    context={};
    return render(request,"account/signup.html",context)




def signup_complete(request):
    context={}
    try:
        user = User.objects.create_user(username=request.POST.get('id'),password=request.POST.get('password'))
    except IntegrityError:
        context.update({"error": "이미 가입된 계정입니다"})
        return render(request, "account/signup.html", context)
    user.email=request.POST["email"]
    major1=request.POST["major1"]
    major2 = request.POST["major2"]
    profile=Profile(user=user,major1=major1,major2=major2)
    user.save()
    profile.save()
    context.update({"user":user})

    return render(request,"account/signup_complete.html",context)


#login함수
def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            context = {}
            context.update({'user': user})
            return  render(request,'home/main.html',context)
        else:
            return render(request,'account/login.html',{'error':'아이디 혹은 비밀번호가 틀렸습니다.'})
    return render(request,'account/login.html')

#logout함수
def logout(request):
    auth.logout(request)
    return render(request,'home/main.html')

