from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1> Hello World!</h1>") # this return a string which is inside HttpResponse
    return render(request, "home.html")

def contact_view(request, *args, **kwargs):

    #return HttpResponse("<h1> This is a contact page.</h1>\n This is the current user: {}".format(request.user))
    return render(request, "contact.html")
   

def something_view(*args, **kwargs):
    return HttpResponse("<h1> Hello World!</h1>")