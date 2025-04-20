from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
seasonly_schedule={
    'Winter':'Thandi',
    'Spring':'Humidity',
    'Summer':' Very Garmi',
    'Rainy':'Paus Wet',
}

def season_schedule_number(request,season):
    seasonlist = list(seasonly_schedule.keys())
    print(seasonlist)

    if (season > len(seasonlist)):
       return HttpResponseNotFound("This season is not available")
    
    redirectseason = seasonlist[season-1]
    print(redirectseason)

    redirectpath = reverse('season-url',args=[redirectseason])
    return HttpResponseRedirect(redirectpath)

def season_schedule(request,season):
    try:
      detail_text = seasonly_schedule[season]
      return HttpResponse(detail_text)
    except:
        return HttpResponseNotFound("This season is not available / Check the URL")
