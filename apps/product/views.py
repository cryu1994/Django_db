from django.shortcuts import render
from .models import Product

def index(request):
    Product.objects.create(name="Ipod",description="Good Condetion",weight="20",price="300",cost="330",category = "Computer")
    product = Product.objects.all()
    print (product)
    return render(request, "index/index.html")
# Create your views here.
