from django.urls import path, include

from .views import *
from . import views
 
urlpatterns = [

path('Monitor_search',views.Monitor_search, name='Monitor_search'),
path('Monitor_home',views.Monitor_home, name='Monitor_home'),
]