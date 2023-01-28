from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path

#from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


urlpatterns = [
    path('',views.getData),
    path('add/', views.addItem),
    # path('Update/', views.UpdateItem),
    path('Update/<pk>/', views.UpdateItem),
    path('getresource/',views.getResource),
   # path('login/', login),
    path('hello/', views.HelloView.as_view(),name='hello'),
    path('monitor_list/', views.Monitor_list),
    #path('apitoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    #path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'),
    #path('verifytoken/',TokenVerifyView.as_view(),name='token_verify')

    
]
