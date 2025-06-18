from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Prodregister


# Create your views here.
# def productlist(request):
#     return render(request, 'products/productlist.html')

def produregister(request):
    if request.method == 'POST':
        form = Prodregister(request.POST)

        if form.is_valid():
            form.save() #save form to db without writing the fields here
            return HttpResponseRedirect('/thank-you')

    form = Prodregister()
    return render(request, 'products/productregistration.html',{
        'form':form
    })

def thankYou(request):
    return render(request, 'products/thank_you.html')