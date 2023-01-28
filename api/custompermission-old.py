from rest_framework import permissions

from django.http import HttpRequest

from djangosite import settings





class SafelistPermission(permissions.BasePermission):

    def has_permission(self,request,view):

        ip_addr = request.META['REMOTE_ADDR']
        print (ip_addr)

        for valid_ip in settings.REST_SAFE_LIST_IPS:

            if ip_addr == valid_ip or ip_addr.startswith(valid_ip):

                return True

        return False

