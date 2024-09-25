import qrcode
from flask import Flask, render_template, send_file
import os

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_qr/<string:amount>/<string:phone>')
def generate_qr(amount, phone):
    # Construct the payment URL (You may need to adjust this according to MPesa's API)
    payment_url = f"https://mpesa.com/pay?amount={amount}&phone={phone}"

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(payment_url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    # Save the QR code image
    img_path = "payment_qr.png"
    img.save(img_path)

    # Return the image
    return send_file(img_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
