from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index),
    path('home/',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('video/',views.video),
    path('gallery/',views.gallery),
    path('blog/',views.blog),
    path('membership/',views.membership),
    path('donate/',views.donate),
    path('',views.index),
    path('causes/',views.causes),
    path('details/',views.vdodetails),
    path('eventdetails/',views.evdetails),
    path('bdetails/',views.blogdetail),
    path('sdetails/',views.sldetails),
    path('myprofile/',views.myprofile),
    path('login/', views.login),
]
