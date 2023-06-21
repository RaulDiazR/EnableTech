import vision
import main


while True:
   mode = input('Escoge el modo que deseas:\n1. Control por voz y Teclado\n2. Control por visión\n')
   if mode == "1":
      main.start()
   elif mode == "2":
      vision.facial_tracking()
   else:
      print("Escoga una opción válida")
      