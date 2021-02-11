# Python program to generate QR code 
#from qrtools import QR 
import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
def generate():
	car = '"regno":"011238", "owener name":"indian__tech__","owener mob":"0123456789"'
	qr = pyqrcode.create(car)
	qr.png("first5.png",scale=8)

def scan():
	  
	# decodes the QR code and returns True if successful 
	all_data = decode(Image.open("first5.png"))
	  
	# prints the data 
	print (all_data)
	print(all_data[0].data.decode("ascii"))
#generate()
scan()