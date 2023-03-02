from django.shortcuts import render, redirect, HttpResponse
from . models import Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']
        if len(name) < 2 or len(email) < 3:
            print("Name is too sort")
        else:
            contact = Contact(name=name, email=email, content=content)
            contact.save()
            print("Form submitted successfully")
    return render(request, 'contact.html')

def handleSignup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        # Check the Input
        if len(username) > 10:
            print("invalid username")
            messages.error(request, 'invalid username')
            return redirect("/")
        
        if not username.isalnum():
            messages.error(request, 'username should be alpha numeric')
            print("username should be alpha numeric")
            return redirect("/")
        
        if pass1 != pass2:
            messages.error(request,'Pass1 and Pass2 not matched')
            print("Pass1 and Pass2 not matched")
            return redirect("/")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'User already exist')
            print("User already exist")
            return redirect("/")
        
        #Create the User
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'User created Successfully')
        print("User created Successfully")
        return redirect("/")
    
    else:
        return HttpResponse('404 - Not Found')
    
def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        
        user = authenticate(username=loginusername, password=loginpass)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successfull')
            print("Login successfull")
            return redirect("/")
        else:
            messages.error(request, 'Invalid username or password')
            print("Invalid username or password")
            return redirect("/")

def handleLogout(request):
    logout(request)
    messages.success(request, 'Logout Successfully')
    print("Logout Successfully")
    return redirect("/")
    return HttpResponse('handleLogout')