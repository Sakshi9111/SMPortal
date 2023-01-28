from django.urls import path, include

from .views import *
from . import views
 
urlpatterns = [
   # path('monitor', views.monitor, name='monitor'),
   #path('iissite', views.iissite, name='iissite'),
   # path('home', views.home, name='home'),
    path('home',views.home, name='home'),
    

    path('search',views.search, name='search'),
    
    path('notifications',feed, name='notifications'),
    path('send-mail', views.SendMail, name='sendmail'),
   ]
    


