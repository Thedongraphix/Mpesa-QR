M-Pesa QR Code Payment Integration
This project demonstrates how to integrate Safaricom's M-Pesa payment system using QR codes. The QR codes generated allow users to initiate payments directly from their M-Pesa account by scanning the QR code. The application utilizes Safaricom's Daraja API for QR code generation.

Table of Contents
Features
Technologies Used
Setup Instructions
Environment Variables
Usage
API Endpoints
License
Features
Generate M-Pesa payment QR codes using the Daraja API.
Integrate M-Pesa payments seamlessly into your Python/Flask application.
Retrieve and display dynamic QR codes.
Sandbox environment for testing M-Pesa transactions.
Technologies Used
Python (Flask) for the backend.
HTML for the frontend.
Requests for making API calls to Safaricom's Daraja API.
Safaricom Daraja API for generating the QR code and handling M-Pesa payments.
Setup Instructions
Clone the Repository
bash
Copy code
git clone https://github.com/Thedongraphix/Mpesa-QR.git
cd Mpesa-QR
Create a Virtual Environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies
bash
Copy code
pip install -r requirements.txt
Environment Variables
Create a .env file in the root directory and add the following keys:

bash
Copy code
DARAJA_CONSUMER_KEY=<your_consumer_key>
DARAJA_CONSUMER_SECRET=<your_consumer_secret>
BASE_URL=https://sandbox.safaricom.co.ke/
Usage
Running the Flask Application
bash
Copy code
flask run
By default, the application will run on http://127.0.0.1:5000/.

Generate QR Codes
Open your browser and navigate to http://127.0.0.1:5000/.
The home route will display the generated M-Pesa QR code for payment.
API Endpoints
1. Generate Access Token
Endpoint: /oauth/v1/generate?grant_type=client_credentials
Method: GET
Description: This endpoint retrieves an access token for authenticating API requests.
2. Generate QR Code
Endpoint: /mpesa/qrcode/v1/generate
Method: POST
Body:
json
Copy code
{
  "amount": 1000,
  "billRefNumber": "12345678",
  "shortCode": "600000"
}
Description: Generates a QR code for M-Pesa payments based on the amount and reference number provided.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

