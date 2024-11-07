from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    if request.method=='POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose another username.')
        elif User.objects.filter(email=email).exists():
            messages.error(request,'Email address is already in use. Please use another email.')
        elif password1==password2:
            user=User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                first_name=firstname,
                last_name=lastname
            )
            login(request,user)
            messages.success(request, "You have registered successfully!")
            return redirect('home')
        else:
            messages.error(request, "Passwords do not match.Please try again!")
    return render(request, 'blog/register.html')



def signin(request):
    if request.method=="POST":
        username = request.POST.get('username')  
        password = request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.error(request, "Invalid UserName or Password")
            return redirect('signin')
        
    return render(request,'blog/signin.html')

def signout(request):
    logout(request)
    return redirect('home')