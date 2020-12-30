import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = '//usersanete/PycharmProjects/Tesseract-OCR/tesseract.exe'
img = Image.open('res/android_test.png')
text = pytesseract.image_to_string(img)
print(text)