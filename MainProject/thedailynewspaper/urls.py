from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('home/',views.home),
    path('index/',views.home),
    path('about/',views.about),
    path('contactus/',views.contactus),
    path('viewnews/',views.viewnews),
    path('videos/',views.videos),
    path('register/',views.register),
    path('viewmore/',views.viewmore),
    path('publish/',views.publish),
]