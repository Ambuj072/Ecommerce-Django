from django.shortcuts import render
from django.contrib import messages
from ecommerceapp.models import Contact

# Create your views here.

def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        desc=request.POST.get("desc")
        myquery=Contact(name=name,email=email,desc=desc)
        myquery.save()
        messages.info(request,"We will get back to you soon..")
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')
