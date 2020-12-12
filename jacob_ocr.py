import pytesseract as tess
from PIL import Image
import os

def ocr():
    tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    path = str(input("Enter file path here "))
    img = Image.open(path,mode='r')
    text = tess.image_to_string(img)
    print(text)
ocr()    