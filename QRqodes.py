# Generate QRCode
import pyqrcode
print("Which URL should be converted into a QR Code")
getUrl = input()
url = pyqrcode.create(getUrl, error='H')
url.png("Output/QRCodeOut.png", module_color=(0, 255, 0, 255), background=(0, 0, 0, 255), scale=5)
print("Done!")

# Decode CRQode
from PIL import Image
from pyzbar.pyzbar import decode
print("Which image should be decoded?")
decode = input()
data = decode(Image.open(decode))
print(data)
print("Done!")