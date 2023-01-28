from .models import ip_token

all_token = ip_token.objects.all
print(all_token)