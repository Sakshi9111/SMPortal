import imp
import re
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from base.models import Item
from display.models import User
from Monitor.models import MonitorItem
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from .serializers import ItemSerializer, MonitorItemSerializer, displaySerializer
from .serializers import ResourceSerializer
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from api.custompermission import BlocklistPermission
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from ip_token.models import ip_token


# @csrf_exempt
# @api_view(["GET"])
# @permission_classes((AllowAny,))
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     if username is None or password is None:
#         return Response({'error': 'Please provide both username and password'},
#                         status=HTTP_400_BAD_REQUEST)
#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response({'error': 'Invalid Credentials'},
#                         status=HTTP_404_NOT_FOUND)
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key},
#                     status=HTTP_200_OK)


@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    #authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [MyPermission]
    return Response(serializer.data)


@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def UpdateItem(request,pk):
    try: 
        ponitorItem = User.objects.get(pk=pk)
    except User.DoesNotExist: 
        return JsonResponse({'message': 'The data does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'PUT':
        monitor_data = JSONParser().parse(request)
        monitor_serializer = displaySerializer(ponitorItem, data=monitor_data) 
        if monitor_serializer.is_valid():
            monitor_serializer.save()
            return JsonResponse(monitor_serializer.data) 
        return JsonResponse(monitor_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

        
@api_view(['POST'])
def Monitor_list(request):
    serializer = displaySerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def getResource(request):
    serializer = ResourceSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

class HelloView(APIView):
    # <-------- Only authenticated users can access this view
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        all_token = ip_token.objects.all
        # print(all_token)
        # <------ Response to the client
        context = {"message": "Hello, World!"}
        return Response(context, {all_token})
