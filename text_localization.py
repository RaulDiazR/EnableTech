import pytesseract as tess
import cv2

from pytesseract import Output

#indicar path de donde esta instalado pytesseract
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'




#Load Image and extract the data
filename = 'texto_compu.png'
image = cv2.imread(filename)

#Convert image to dictionary

results = tess.image_to_data(image, output_type=Output.DICT)

print(results)