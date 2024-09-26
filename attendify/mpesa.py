import requests
import base64
from datetime import datetime

def initiate_stk_push(phone_number, amount):
    
    consumer_key = 'your_consumer_key'
    consumer_secret = 'your_consumer_secret'
    business_short_code = 'your_short_code'
    passkey = 'your_passkey'
    lipa_na_mpesa_online_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'

    
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    password = base64.b64encode((business_short_code + passkey + timestamp).encode()).decode('utf-8')

    access_token = get_access_token(consumer_key, consumer_secret)
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    payload = {
        "BusinessShortCode": 4742552,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": business_short_code,
        "PhoneNumber": phone_number,
        "CallBackURL": "https://yourdomain.com/callback_url",
        "AccountReference": "Event Registration",
        "TransactionDesc": "Payment for event registration"
    }

    response = requests.post(lipa_na_mpesa_online_url, json=payload, headers=headers)
    if response.status_code == 200:
        return {'status': 'success', 'reference': response.json().get('CheckoutRequestID')}
    else:
        return {'status': 'failed'}

def get_access_token(consumer_key, consumer_secret):

    auth_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    response = requests.get(auth_url, auth=(consumer_key, consumer_secret))
    return response.json()['access_token']
