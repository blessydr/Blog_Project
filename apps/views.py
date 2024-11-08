from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Blogs_post,Tag
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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


def index(request):
    search = request.GET.get('search', '')
    
    if search:
        blogs = Blogs_post.objects.filter(
            Q(title__icontains=search) | 
            Q(description__icontains=search) | 
            Q(tags__blog_tag__icontains=search)
        ).distinct()
    else:
        blogs = Blogs_post.objects.all() 

   
    tags = Tag.objects.all()

   
    context = {
        'blogs': blogs,
        'tags': tags,
        'search': search
    }
    return render(request, 'blog/home.html', context)



def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        tags = request.POST.getlist('tags')  
        image = request.FILES.get('image') 

      
        if not title or not description:
            messages.error(request, "Title and description are required.")
            return redirect('create_blog')  
      
        blog = Blogs_post.objects.create(
            title=title,
            description=description,
            author=request.user,  
            images=image
        )

        if tags:
            for tag_id in tags:
                tag = Tag.objects.get(id=tag_id)
                blog.tags.add(tag)
        
       
        blog.save()

     
        messages.success(request, "Your blog has been created successfully!")
        return redirect('home') 

   
    tags = Tag.objects.all()  
    return render(request, 'blog/create_blog.html', {'tags': tags})


def blog_details(request,pk):
    blog = Blogs_post.objects.get(id=pk)
    context = {'blog': blog}
    return render(request, 'blog/blog_details.html', context)