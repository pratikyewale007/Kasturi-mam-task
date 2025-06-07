from django.urls import path
from .import views

urlpatterns = [
    path('<int:month>',views.month_schedule_number),
    path('<str:month>',views.month_schedule,name='month-url'),
]