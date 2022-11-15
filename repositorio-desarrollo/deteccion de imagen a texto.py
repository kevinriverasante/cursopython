##Pillow 9.3.0
##pytesseract 0.3.10
from PIL import Image
from pytesseract import *
pytesseract.tesseract_cmd = r'C:\Users\NINIVE RIVERA\AppData\Local\Tesseract-OCR\tesseract.exe'

img = Image.open("Image.png")

resultado = pytesseract.image_to_string(img, lang="spa")
print(resultado)
