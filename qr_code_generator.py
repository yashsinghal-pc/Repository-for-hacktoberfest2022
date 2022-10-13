# QR Code Generator

import pyqrcode 
from pyqrcode import QRCode 
  
# URL 
url = "https://www.innotechzz.com/"
  
# Generating QR code 
qr = pyqrcode.create(url) 

# Saving the QR code
qr.svg("qr.svg", scale=8)
