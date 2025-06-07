from django.urls import path
from .import views

urlpatterns = [
    path('<int:week>',views.week_schedule_number),
    path('<str:week>',views.week_schedule,name='week-url'),
]