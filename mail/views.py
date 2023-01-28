from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from djangosite import settings
from ip_token.models import ip_token 
import datetime
from base.models import Item



# Create your views here.

def home(request):
    return render(request,'notifications.html')

def SendMail(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        msg=request.POST.get('msg')
        subject='Welcome to Spiralogics Portal'
        message=msg
        from_email=settings.EMAIL_HOST_USER
        recipent_list=['roshan.shah.rauniyar@gmail.com','roshan.shah20171@gmail.com']
        send_mail(subject,message,from_email,recipent_list,fail_silently=True)

        return HttpResponse('Alerted')

def feed(request):
    all_tokens=ip_token.objects.all()   
    #token_data=ip_token.objects.all()            
    data={
        'Token_Data': all_tokens
    }
    return render(request,'notifications.html',data)

# def feed(request):
#     #all_items = Item.objects.all()
#     #form=DateformClass()
#     if request.method=="GET":
#          st=request.GET.get('server')
         
#          now = datetime.datetime.now()
#          earlier = now - datetime.timedelta(minutes=45)
#          all_items=Item.objects.filter(Created__range=(earlier,now),ServerName=st) 
         

#     data={
#         'All_items': all_items,
#         #'form':form
   
#     }
    
#     return render(request,'notifications.html',data)

# test = Item.objects.all()
# print(test)