import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

CONSUMER_KEY = os.getenv("uJ5caIxhTKwjNHIjInAuCPFR9OkovAKXYkBlUk10Cc4Yi6cF")
CONSUMER_SECRET = os.getenv("T5WtAPuhggOqKRYLyMdeNNe97SNJ0vGGeB3gdu2pcB2ZvxcgdBgTEgIDA681tEid")
BASE_URL = os.getenv("https://sandbox.safaricom.co.ke/")

def generate_access_token():
    """
    Generate an access token from the Daraja API
    """
    api_url = f'{BASE_URL}oauth/v1/generate?grant_type=client_credentials'
    auth = HTTPBasicAuth(CONSUMER_KEY, CONSUMER_SECRET)
    response = requests.get(api_url, auth=auth)
    
    if response.status_code == 200:
        access_token = response.json()['access_token']
        return access_token
    else:
        raise Exception(f"Failed to get access token: {response.status_code} {response.text}")

def generate_qr_code():
    """
    Generate an M-Pesa QR code for a payment
    """
    access_token = generate_access_token()
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    # Define QR code generation endpoint
    api_url = f'{BASE_URL}mpesa/qrcode/v1/generate'

    # Body parameters for QR code generation
    qr_data = {
        "amount": 1000,  # The payment amount
        "billRefNumber": "12345678",  # Use any reference
        "shortCode": "600000"  # This is the Safaricom test shortcode for sandbox
    }

    response = requests.post(api_url, json=qr_data, headers=headers)
    
    if response.status_code == 200:
        qr_code_data = response.json()
        print("QR Code Generated:", qr_code_data)
        return qr_code_data
    else:
        raise Exception(f"Failed to generate QR code: {response.status_code} {response.text}")

if __name__ == "__main__":
    generate_qr_code()
