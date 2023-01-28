from django.urls import path
 
from . import views
 
urlpatterns = [
    #path('', views.index, name='index'),
    path('iissite', views.iissite, name='iissite'),
   #path('home', views.home, name='home'),

]

