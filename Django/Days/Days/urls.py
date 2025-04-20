from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('month/',include('month.urls')),
    path('week/',include('week.urls')),
    path('season/',include('season.urls')),
]
