from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
weekly_schedule={
    'Monday':'Games',
    'Tuesday':'Football',
    'Wednesday':'Cricket',
    'Thursday':'Volleyball',
    'Friday':'Basketball',
    'Saturday':'Cycling',
    'Sunday':'OFF',
}

def week_schedule_number(request,week):
    week_list = list(weekly_schedule.keys())
    print(week_list)

    if (week > len(week_list)):
        return HttpResponseNotFound("Invalid week number")
    
    redirectweek = week_list[week-1]
    print(redirectweek)

    redirectpath = reverse('week-url', args=[redirectweek])
    return HttpResponseRedirect(redirectpath)

def week_schedule(request,week):
    try:
        details=weekly_schedule[week]
        return HttpResponse(details)
    except:
        return HttpResponseNotFound('The week you entered is not proper / Plz Check URL')
