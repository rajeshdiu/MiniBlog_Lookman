from django.shortcuts import redirect, render
from .models import Post
from .forms import SignUpForm,LoginFrom
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

# home
def home(request):
    posts = Post.objects.all()
    return render(request,'home.html',{"posts":posts})

# Contact Page
@login_required
def contact(request):
    return render(request,'contact.html')

# About Page
def about(request):
    return render(request,'about.html')

# Dashboard page
@login_required
def dashboard(request):
    posts = Post.objects.all()
    # user = request.user
    # full_name = user.get_full_name()
    # gps = user.groups.all()
    return render(request,'dasboard.html',{'posts':posts})


# Sign UP page
def signupPage(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations !! You have become a author ✔✔👍')
            form.save()
        else:
            messages.error(request,"InValid Password or Username or This username has been taken.")
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})


# Login Page
def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginFrom(request=request,data= request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = auth.authenticate( username = uname,password = upass)
                if user != None:
                    auth.login(request,user)
                    # login(request,user)
                    messages.success(request,'Successfully logged In ✔✔👍')
                    return redirect('dashboard')
                else:
                    messages.error(request,'username or password is invalid')
        else:
            form = LoginFrom()
            return render(request,'login.html',{'form':form})
    else:
        return redirect('dashboard')
# Logout Page
def logoutPage(request):
    logout(request)
    return redirect('login')
    