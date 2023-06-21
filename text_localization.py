
import pyTesseract as tess
from pyTesseract import Output

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

import cv2


#Load Image and extract the data
filename = 'texto_compu.png'
image = cv2.imread(filename)

#Convert image to dictionary

results = tess.image_to_data(image, output_type=Output.DICT)

print(results)