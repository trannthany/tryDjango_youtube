from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1> Hello World!</h1>") # this return a string which is inside HttpResponse
    my_context = {
        "my_text"   : "This is about us",
        "my_number" : 123,
        "my_list"   : [123, 24, 26, 27, 30, 32]
    }
    return render(request, "home.html", my_context)

def contact_view(request, *args, **kwargs):

    #return HttpResponse("<h1> This is a contact page.</h1>\n This is the current user: {}".format(request.user))
    return render(request, "contact.html")
   

def something_view(*args, **kwargs):
    return HttpResponse("<h1> Hello World!</h1>")