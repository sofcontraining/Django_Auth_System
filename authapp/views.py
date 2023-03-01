from django.shortcuts import render, redirect, HttpResponse
from . models import Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

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
            return redirect("/")
        
        if not username.isalnum():
            print("username should be alpha numeric")
            return redirect("/")
        
        if pass1 != pass2:
            print("Pass1 and Pass2 not matched")
            return redirect("/")
        
        if User.objects.filter(username=username).exists():
            print("User already exist")
            return redirect("/")
        
        #Create the User
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        print("User created Successfully")
        return redirect("/")
    
    else:
        return HttpResponse('404 - Not Found')