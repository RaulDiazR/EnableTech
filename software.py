import vision
import main

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QEvent, QObject


def button1_click():
    try:
      main.start()
      label.setText("Saliste del Modo Voz,\nescoga una opción")
    except KeyboardInterrupt:
        print("Saliste del Modo Voz")
        label.setText("Saliste del Modo Voz,\nescoga una opción")


def button2_click():
   vision.facial_tracking()
   label.setText("Saliste del Modo Visual,\nescoga una opción")


def exit_program():
    # Close the application
    app.quit()


class ButtonPressFilter(QObject):
    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            key = event.key()
            if key == Qt.Key_1:
                button1.click()
                return True
            elif key == Qt.Key_2:
                button2.click()
                return True
            elif key == Qt.Key_3:
                exit_button.click()
                return True 
        return super().eventFilter(obj, event)


# Create the application
app = QApplication([])

# Create a main window
window = QMainWindow()
window.setWindowTitle("Software")
window.setGeometry(100, 100, 300, 310)

# Create buttons
button1 = QPushButton("Control de Voz y Teclado", window)
button1.setGeometry(50, 120, 200, 40)
button1.clicked.connect(button1_click)

button2 = QPushButton("Control Visual", window)
button2.setGeometry(50, 170, 200, 40)
button2.clicked.connect(button2_click)

exit_button = QPushButton("Salir", window)
exit_button.setGeometry(50, 220, 200, 40)
exit_button.clicked.connect(exit_program)

# Create a label
label = QLabel("Escoga una de las\n siguientes opciones:", window)
label.setAlignment(Qt.AlignCenter)
label.setGeometry(50, 20, 220, 80)

# Set font type and size for the label
font = QFont("Arial", 14, QFont.Bold)  # Change the font type and size here
label.setFont(font)

# Set a custom style for the buttons
button_style = """
    QPushButton {
        color: white;
        font-size: 14px;
        border-radius: 30px;
        border: none;
    }
    QPushButton#button1 {
        background-color: blue;
    }
    QPushButton#button1:hover {
        background-color: darkblue;
    }
    QPushButton#button2 {
        background-color: green;
    }
    QPushButton#button2:hover {
        background-color: darkgreen;
    }
    QPushButton#exit_button {
        background-color: red;
    }
    QPushButton#exit_button:hover {
        background-color: #8b0000;
    }
"""
button1.setObjectName("button1")
button2.setObjectName("button2")
exit_button.setObjectName("exit_button")

button1.setStyleSheet(button_style)
button2.setStyleSheet(button_style)
exit_button.setStyleSheet(button_style)

# Install the event filter to the application
button_press_filter = ButtonPressFilter()
app.installEventFilter(button_press_filter)

# Show the window
window.show()

# Run the application event loop
app.exec_()
