from django.urls import path
from .import views

urlpatterns = [
    path('<int:season>',views.season_schedule_number),
    path('<str:season>',views.season_schedule,name='season-url'),
]