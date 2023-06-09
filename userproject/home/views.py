from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import logout, authenticate,login

# Create your views here.
def index(request):
   if request.user.is_anonymous:
        return redirect('/login')
   return render(request,'index.html')

def loginuser(request):
   if request.method=="POST":
      #Check if user has entered correct credentials or not
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)

        if user is not None:

         #A backend authenticated the credentials
            print(request.user)
            login(request,user)
            print(request.user)
            return redirect('/')
        else:
            return render(request,'login.html')     
   else:
      return render(request,'login.html')
        

def logoutuser(request):
    logout(request)
    return redirect("/login")