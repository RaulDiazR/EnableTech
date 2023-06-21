from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode, Key
import sys
import os
import pyautogui
import recordvoice
#from text_localization import x, y, w, h


mouse = Controller()
mouseControl = True

#if x != None:
 #  mouse.position((x+(w/2)), (y+(h/2)))

def on_press(key):
   global mouseControl
   if mouseControl:
      # tecla izquierda
      if key == KeyCode(char='a'):
         mouse.move(-10, 0)
      # tecla inferior
      elif key == KeyCode(char='s'):
         mouse.move(0, 10)
      # tecla derecha
      elif key == KeyCode(char='d'):
         mouse.move(10, 0)
      # tecla superior
      elif key == KeyCode(char='w'):
         mouse.move(0, -10)
      # Click izquierdo
      elif key == KeyCode(char='o'):
         mouse.click(Button.left)
            # tecla izquierda
      if key == Key.left:
         mouse.move(-10, 0)
      # tecla inferior
      elif key == Key.down:
         mouse.move(0, 10)
      # tecla derecha
      elif key == Key.right:
         mouse.move(10, 0)
      # tecla superior
      elif key == Key.up:
         mouse.move(0, -10)
      # Click izquierdo
      elif key == Key.caps_lock:
         mouse.click(Button.left)
      # Click derecho     
      elif key == Key.shift_r:
         mouse.click(Button.right)  
      # Desabilitar Control de Mouse
      elif key == Key.ctrl_r:
         mouseControl = not mouseControl
      # Salir del Modo Keyboard Listener
      elif key == Key.space:
         filename = f"screenshot.png"
         screenshot = pyautogui.screenshot()
         screenshot.save(filename)
         recordvoice.record()
         
      elif key == Key.esc:
         return False 
      
   # Desabilitar Control de Mouse
   elif key == Key.ctrl_r:
      mouseControl = not mouseControl
   # Salir del Modo Keyboard Listener
   elif key == Key.esc:
      return False  
   

print("Press esc to stop the mouse movement.")
with Listener(on_press=on_press) as listener:
    listener.join()

def coordenates(x, y, w, h):
   cx = x
   cy = y
   cw = w
   ch = h
   on_press()