from ip_token.models import ip_token

all_token = ip_token.objects.ips()
abc = all_token.json
print(abc)

