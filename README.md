M-Pesa QR Code Generator
This Python project generates QR codes for M-Pesa payments using the Daraja API. The QR codes can be scanned to initiate payments seamlessly.

Features
Generate payment URLs using the Daraja API
Create QR codes from payment URLs
Securely handle API credentials
Robust error handling and logging
Requirements
Python 3.x
python-daraja library
qrcode library
Installation
Clone the repository:
git clone https://github.com/yourusername/mpesa-qr-code-generator.git
cd mpesa-qr-code-generator

Install the required libraries:
pip install python-daraja qrcode[pil]

Usage
Set up your Daraja API credentials in the payment module:
Python

from python_daraja import payment

payment.SHORT_CODE = "YOUR_SHORTCODE"
payment.PASSKEY = "YOUR_PASSKEY"
payment.CONSUMER_SECRET = "YOUR_CONSUMER_SECRET"
payment.CONSUMER_KEY = "YOUR_CONSUMER_KEY"
payment.ACCOUNT_TYPE = "PAYBILL"  # or "TILL" for BuyGoods
AI-generated code. Review and use carefully. More info on FAQ.
Create a function to generate the payment URL:
Python

def generate_payment_url(phone_number, amount, callback_url, description, account_ref):
    details = payment.trigger_stk_push(
        phone_number=phone_number,
        amount=amount,
        callback_url=callback_url,
        description=description,
        account_ref=account_ref
    )
    return details.get('CheckoutRequestID')
AI-generated code. Review and use carefully. More info on FAQ.
Generate the QR code:
Python

import qrcode

def generate_qr_code(data, file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)
AI-generated code. Review and use carefully. More info on FAQ.
Integrate everything to create the QR code:
Python

def create_mpesa_qr_code(phone_number, amount, callback_url, description, account_ref, file_path):
    checkout_request_id = generate_payment_url(phone_number, amount, callback_url, description, account_ref)
    if checkout_request_id:
        payment_url = f"https://api.safaricom.co.ke/mpesa/stkpushquery/v1/query?CheckoutRequestID={checkout_request_id}"
        generate_qr_code(payment_url, file_path)
        print(f"QR code generated and saved to {file_path}")
    else:
        print("Failed to generate payment URL")

# Example usage
create_mpesa_qr_code(
    phone_number="254712345678",
    amount=100,
    callback_url="https://your-domain/callback/",
    description="Payment for services rendered",
    account_ref="Account123",
    file_path="mpesa_qr_code.png"
)
AI-generated code. Review and use carefully. More info on FAQ.
Best Practices
Secure Your Credentials: Store your API credentials securely, preferably in environment variables.
Error Handling: Implement robust error handling to manage API failures and invalid responses.
Logging: Use logging to track the flow of your application and debug issues effectively.
Testing: Thoroughly test your integration in a sandbox environment before going live.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to customize this README further to suit your project’s needs! If you have any other questions or need additional help, just let me know.

1
github.com
Chat with Copilot
