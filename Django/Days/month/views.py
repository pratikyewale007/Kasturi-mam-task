from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
monthly_schedule={
    'january':'Learn Django',
    'february':'Learn Python',
    'march':'Learn Java',
    'april':'Learn C++',
    'may':'Learn sql',
    'june':'Learn C#',
    'july':'Learn Bootstrap',
    'august':'Learn HTML',
    'september':'Learn CSS',
    'october':'Learn JavaScript',
    'november':'Learn React',
    'december':'Learn Angular',
}

def month_schedule_number(request,month):
    monthlist = list(monthly_schedule.keys())
    print(monthlist)

    if(month > len(monthlist)):
        return HttpResponseNotFound("Invalid month number")
    
    redirectmonth = monthlist[month-1]
    print(redirectmonth)

    redirectpath = reverse('month-url',args=[redirectmonth])
    return HttpResponseRedirect(redirectpath)
    
def month_schedule(request,month):
    try:
        detail_text = monthly_schedule[month]
        return HttpResponse(detail_text)
    except:
        return HttpResponseNotFound('This month is not supported / Check the url')