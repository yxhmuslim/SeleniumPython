#coding=utf-8
import pytesseract
from PIL import Image
image=Image.open("e://imooc2.png")
text=pytesseract.image_to_string(image)
print(text)