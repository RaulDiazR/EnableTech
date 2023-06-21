

import pytesseract as tess

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

from PIL import Image

img = Image.open('texto_compu.png')

text = tess.image_to_data(img)


print(text)