from dataclasses import field
from importlib.resources import Resource
from rest_framework import serializers
from base.models import Item 
from Monitor.models import MonitorItem
from display.models import User


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class MonitorItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitorItem
        fields = '__all__'
class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'
class displaySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
