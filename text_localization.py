import pytesseract as tess
import cv2
from pytesseract import Output

def scan():
   #indicar path de donde esta instalado pytesseract
   #tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   tess.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"

   #Load Image and extract the data
   filename = 'screenshot.png'
   image = cv2.imread(filename)

   #Convert image to dictionary
   results = tess.image_to_data(image, output_type=Output.DICT)

   #define cont to read multiple coords
   cont = 0
   #print(results)
   with open('output.wav.txt') as f:
       lines = f.readlines()

   result = lines[0].split(" ")
   word = str(result[0])

   result = lines[0].split(".")
   word = str(result[0])

   wordlower = word.lower()
   #Extract bounding coordinates
   for i in range(0, len(results["text"])):
      x = results["left"][i]
      y = results["top"][i]

      w = results["width"][i]
      h = results["height"][i]

      text = results["text"][i]
      conf = int(results["conf"][i])


      if conf > 50 and text == word:

         text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
         cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 200), 2)
       #Print coordinates of the chosen word
         print(f"Coordenadas en x({cont}): {x}")
         print(f"Coordenadas en y({cont}): {y}")
         print(f"Anchura({cont}): {w}")
         print(f"Altura({cont}): {h}")
         cont += 1
         print("\n")
         coords = [x, y, w, h]
         f.close()
         print(word)
         print(coords)
         return coords