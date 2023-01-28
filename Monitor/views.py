from django.shortcuts import render
from ip_token.models import ip_token 
import datetime
from .models import MonitorItem

# Create your views here.
def Monitor_home(request):
    # all_tokens=ip_token.objects.all()   
    #token_data=ip_token.objects.all()  
    all_tokens = MonitorItem.objects.all()   
    print(all_tokens)       
    data={
        'Token_Data': all_tokens
    }
    return render(request,'Monitor_home.html',data)

def Monitor_search(request):
    #all_items = Item.objects.all()
    #form=DateformClass()
    if request.method=="GET":
         st=request.GET.get('Name')
         now = datetime.datetime.now()
         earlier = now - datetime.timedelta(minutes=45)
         all_items=MonitorItem.objects.filter(Created__range=(earlier,now),Name=st) 

    data={
        'All_items': all_items,
        #'form':form
    }
    return render(request,'Monitor_index.html',data)