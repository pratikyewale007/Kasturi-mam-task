from django.shortcuts import render
from .models import Products

# Create your views here.
def productlist(request):
    products = Products.objects.all()
    return render(request, 'products/productlist.html', 
                {
                  'products': products
                })