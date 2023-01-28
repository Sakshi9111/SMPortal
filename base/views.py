from django.shortcuts import render, redirect
from .models import Item
from ip_token.models import ip_token 
from datetime import datetime, timedelta
import datetime
from django.shortcuts import render
from django.http import HttpResponse  
from djangosite import settings
from django.core.mail import send_mail





# def monitor(request):
#     all_items = Item.objects.all()
#     return render(request, 'datatable/index.html', {'All_items': all_items})    

# def home(request):
#     #all_servers = ip_token.objects.all()
#     if request.method == "GET":
#         td=request.GET.get('server_name')
#         print(td)
#         if td!=None:
#             all_items=Item.objects.filter(ServerName=td)            
#     data={
#        'all_items': all_items
#     }
#     #print(f'server_data:{server_data}')
#     return render(request, 'datatable/index.html', data)     





#in use
def home(request):
    all_tokens=ip_token.objects.all()   
    #token_data=ip_token.objects.all()            
    data={
        'Token_Data': all_tokens
    }
    return render(request,'datatable/home.html',data)

# def Monitor_home(request):
#     all_tokens=ip_token.objects.all()   
#     #token_data=ip_token.objects.all()            
#     data={
#         'Token_Data': all_tokens
#     }
#     return render(request,'datatable/Monitor_home.html',data)
# def feed(request):
#     all_tokens=ip_token.objects.all()   
#     #token_data=ip_token.objects.all()            
#     data={
#         'Token_Data': all_tokens
#     }
#     return render(request,'templates/notifications',data)


def search(request):
    #all_items = Item.objects.all()
    #form=DateformClass()
    if request.method=="GET":
         st=request.GET.get('server')
         now = datetime.datetime.now()
         earlier = now - datetime.timedelta(minutes=45)
         all_items=Item.objects.filter(Created__range=(earlier,now),ServerName=st) 

    data={
        'All_items': all_items,
        
        #'form':form
    }
    
    return render(request,'datatable/index.html',data)
    

# def Monitor_search(request):
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
#     return render(request,'datatable/Monitor_index.html',data)

def feed(request):
    return render(request,'datatable/notifications.html')

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
        # return render(request,'datatable/notifications.html')


# def mail(request):  
#     subject = "Greetings"  
#     msg     = "Congratulations for your success"  
#     to      = "roshan.shah.rauniyar@gmail.com"  
#     res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
#     if(res == 1):  
#         msg = "Mail Sent Successfuly"  
#     else:  
#         msg = "Mail could not sent"  
#     return HttpResponse(msg)  

# def mail(request):
#     send_mail(
#     'Subject here',
#     'Here is the message.',
#     'roshan.spiralogics@gmail.com',
#     ['roshan.shah.rauniyar@gmail.com'],
#     fail_silently=False,
# )

# def notification(request):
#     return render(request,'database/notifications.html')

# def SendMail(request):
#     if request.method == 'POST':
#         email=request.POST['email']
#         msg=request.POST['msg']
#         subject='Welcome to Spiralogics Portal'
#         message=msg
#         testing = 'helo '
#         from_email=settings.EMAIL_HOST_USER
#         recipent_list=['roshan.shah.rauniyar@gmail.com','roshan.shah20171@gmail.com']
#         send_mail(subject,message,from_email,recipent_list,fail_silently=True)
        

#         return HttpResponse('testing')