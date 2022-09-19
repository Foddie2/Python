#Install all the libraries needed 
#create a function that collects text and convert to a QR code 
#Save the QR code as an image 
#Run the function echo "# Python" >> README.md

from asyncio import constants
import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version= 1,
        error_correction= qrcode.constants.ERROR_CORRECT_l,
        box_size=10,
        border=5    
    )