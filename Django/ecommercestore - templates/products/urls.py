from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.produregister),
    path('thank-you', views.thankYou),
]