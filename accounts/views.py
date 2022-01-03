from django.contrib import messages , auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from posts.models import Post

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.error(request,'The email is already registered')
                return redirect('register')
            
            else:
                user = User.objects.create_user(username = email , password = password , first_name = first_name , last_name = last_name )
                # auth.login(request, user)
                # messages.success(request,'You are now logged in')
                # return redirect('index')
                user.save()
                messages.success(request,'You are now registered and can log in')
                return redirect('login')
        else:
            messages.error(request,'password do not match')
            return redirect('register')
    else:
        return render(request,'pages/signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username = email, password= password)

        if user is not None:
            auth.login(request, user)
            messages.success(request,'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
    else:
        
        return render(request,'pages/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now Logged Out')
        return redirect('login')

def dashboard(request):
    logged_in_user = request.user
    logged_in_user_post = Post.objects.filter(author = logged_in_user)
    return render(request,'pages/dashboard.html',{'logged_in_user_post':logged_in_user_post})

def Total_posts(request):
    logged_in_user = request.user
    logged_in_user_post = Post.objects.filter(author = logged_in_user).count()
    return render(request,'pages/dashboard.html',{'logged_in_user_post':logged_in_user_post})
