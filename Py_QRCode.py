import pyqrcode
from pyqrcode import QRCode

QRString = r"https://github.com/RicardoHenriqueSantos"

print(QRString)

url = pyqrcode.create(QRString)

url.png(r"qr.png", scale=8)
