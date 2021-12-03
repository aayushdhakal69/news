from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from home.models import Contact
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def contact(request):
    if request.method=='POST':
        name= request.POST['name']
        email= request.POST['email']
        content= request.POST['content']
        if len(name)<2 or len(email)<3 or len(content)<5:
            messages.error(request, "Please fill the form correctly")
        else:
            contact= Contact(name= name, email=email, content= content)
            contact.save()
            messages.success(request, "Thank you for your feedback, your message has been successfully sent.")
    
    return render(request, 'home/contact2.html/')

def about(request):
    return render(request, 'home/about3.html')

def blogHome(request):
    return render(request,'templates/blog/blogHome.html')

