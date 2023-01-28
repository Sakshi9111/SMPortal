from django.urls import path
from display import views as display


urlpatterns = [
    path('', display.index, name="index"),
    path('ajax/getList', display.getList, name="getList"),
    path('updateUser/<pk>', display.updateUser.as_view(), name="updateUser"),
    path('deleteUser/<pk>', display.deleteUser.as_view(), name="deleteUser"),
    
]