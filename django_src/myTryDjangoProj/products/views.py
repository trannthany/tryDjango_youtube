from django.shortcuts import render
from .models import Product

# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1) #the objects id is created automatically by django inside 0001_initial.py (migration)
    # context = {
    #     "title"         : obj.title,
    #     "description"   : obj.description
    # } # this give extra steps

    context = {
        'object': obj
    }# this removes the extra steps

    return render(request, "product/detail.html", context)

     
# {% block content %}
# <h1> {{title}} </h1>
# <p> {% if description != None and description != '' %}
# {{description}}
# {% else %}
# Description is coming soon
# {% endif %} </p>
# #this has many steps
# {% endblock content %}
