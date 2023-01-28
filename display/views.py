from django.shortcuts import render
from django.http import JsonResponse
from display import models
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import User
from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404



# Create your views here.
def index(request):
    return render(request, 'display/index.html')

# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['MonitorId', 'Name', 'ServerName']

# def getUsers(request):
#     queryset = models.User.objects.all()[:20]
#     return JsonResponse({'users':list(queryset.values()
#     )})
def getList(request):
    mall_tokens=User.objects.all()   
    #token_data=ip_token.objects.all()            
    mdata={
        'mToken_Data': mall_tokens
    }
    return render(request,'display/index.html',mdata)
    
# def updateUser(request, pk, template_name='display/index.html'):
#     contact = get_object_or_404(User, pk=pk)
#     form = UserForm(request.POST or None, instance=contact)
#     if form.is_valid():
#         form.save()
#         return redirect('index')
#     return render(request, template_name, {'form':form})

class updateUser(UpdateView):
    model= models.User
    fields = [ 'Monitor' ]
    success_url = reverse_lazy('getList')

class deleteUser(DeleteView):
    model = models.User
    success_url = reverse_lazy('getList')

