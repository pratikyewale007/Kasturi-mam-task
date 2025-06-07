from django.shortcuts import render

# Create your views here.
def userlist(request):
    return render(request, 'users/userlist.html')