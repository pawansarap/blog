from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from blog.models import Contact
from blog.models import Blog
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def home(request):
    if request.user.is_anonymous:
        return redirect('/login')

    return render(request,'index.html')
    # return HttpResponse("this is home page")
from django.shortcuts import render, redirect, HttpResponse
# Make sure all other necessary imports are here


def loginuser(request):
    # username:- testname
    # # password:- test@2024
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('/')

        else:
            # No backend authenticated the credentials
            messages.error(request, "Please enter the Correct Username and Password!")
            return render(request,'login.html')
   
    return render(request, 'login.html')
    

def logoutuser(request):
    logout(request)
    return  redirect('/login')

# def blog(request):
#      return render(request,'blog.html')

def add_blog(request):
    if request.method == 'POST': 
        title = request.POST.get('blogtitle')
        email = request.POST.get('blogemail')
        desc = request.POST.get('blogdesc')
        thumbnail = request.POST.get('blogthumbnail')

        # Create a new Blogs object with the correct field names and save it
        blog = Blog(blogtitle=title, blogemail=email, blogdesc=desc, blogthumbnail=thumbnail, blogdate=datetime.today())
        blog.save()
        messages.success(request, "Your Blog is added!")
    return render(request, 'add_blog.html')

def blog_view(request):
    # Fetch all blog entries from the Blog model
    blogs = Blog.objects.all() 
    return render(request, 'blog.html', {'blogs': blogs})

def contact(request):
    if request.method == 'POST': #add the validation before upload the site on github
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        contact = Contact(name=name, email=email, phone=phone, desc=desc,date = datetime.today())
        contact.save()
        messages.success(request, "Your Massage has been sent! Thank you for getting in touch.")
    return render(request,'contact.html')       
