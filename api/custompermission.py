from rest_framework import permissions
from djangosite import settings
from rest_framework import exceptions
from ip_token.models import ip_token


class BlocklistPermission(permissions.BasePermission):
    def has_permission(self, request, code=None, view=None):
        message = {
            'message': 'Authentication credentials were not provided',
            'status': 'False'
        }
        ip_addr = request.META.get('REMOTE_ADDR')  # get client ip address
        print(ip_addr)
        auth_token = request.META.get('HTTP_AUTHORIZATION')  # client token
        print(auth_token)
        for valid_ip in settings.REST_SAFE_LIST_IPS:
            if ip_addr == valid_ip or ip_addr.startswith(valid_ip):
                ipop = ip_token.objects.filter(
                    ip=f'{ip_addr}')  # get ip from database
                if not ipop:
                    message_token = {
                        'message': 'No Permission',
                        'status': 'False'
                    }
                    raise exceptions.PermissionDenied(
                        detail=message_token, code=400)

                else:
                    # ip exist
                    first_value = ipop.first()
                    print(first_value)
                    token_value = first_value.token
                    print(token_value)
                    if str(token_value) == str(auth_token):
                        return True
                    else:
                        message_auth = {
                            'message': 'Token did not match',
                            'status': 'False'
                        }
                    raise exceptions.PermissionDenied(
                        detail=message_auth, code=400)

                # if exit:

                # check auth token, if ip exist in database
                  # return true if token matches
                  # else
                  # raise error token doesnot match
                # else

                #raise error (not save in db)

        raise exceptions.PermissionDenied(detail=message, code=400)
