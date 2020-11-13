# pip3 install pytesseract
# sudo apt update
# sudo apt install tesseract-ocr
# sudo apt install libtesseract-dev
# python3 -m pip install tesseract tesseract-ocr pytesseract

import pytesseract
from PIL import Image

img = Image.open("img.png")

extract_image = pytesseract.image_to_string(img)

print("text:\n", extract_image)