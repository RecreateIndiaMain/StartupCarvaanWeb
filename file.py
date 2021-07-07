import requests
import django
from django.http import HttpResponse
id
def payment():
    headers = { "X-Api-Key": "4775c2f06f3d85a5b9cbeb9cfd2eeb69", "X-Auth-Token": "c8e0383df746f9d6f1c87fa1c1cab81e"}
    payload = {
    'purpose': 'FIFA 16',
    'amount': '2500',
    'buyer_name': 'John Doe',
    'email': 'foo@example.com',
    'phone': '8171365728',
    'redirect_url': 'http://www.example.com/redirect/',
    'send_email': 'True',
    'send_sms': 'True',
    'webhook': 'http://www.example.com/webhook/',
    'allow_repeated_payments': 'False',
    }
    response = requests.post("https://www.instamojo.com/api/1.1/payment-requests/", data=payload, headers=headers)
    jsonres=response.json()
    id=jsonres['payment_request']['id']
    return HttpResponse(id)

payment()