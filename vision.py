import cv2
import mediapipe as mp
import pyautogui

def facial_tracking():
    camara = cv2.VideoCapture(0)  # Inicializa la cámara
    lector_puntos_faciales = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)  # Inicializa el modelo de detección de puntos faciales de MediaPipe
    ancho_pantalla, alto_pantalla = pyautogui.size()  # Obtiene el tamaño de la pantalla

    while True:
        _, frame = camara.read()  # Captura un fotograma de la cámara
        frame = cv2.flip(frame, 1)  # Voltea el fotograma horizontalmente

        # Aplica el suavizado a la imagen utilizando un kernel
        frame = cv2.GaussianBlur(frame, (5, 5), 0)

        fotograma_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convierte el fotograma a formato RGB
        resultado = lector_puntos_faciales.process(fotograma_rgb)  # Procesa el fotograma para detectar puntos faciales
        puntos_faciales = resultado.multi_face_landmarks  # Obtiene los puntos faciales detectados
        alto_fotograma, ancho_fotograma, _ = frame.shape  # Obtiene el alto y ancho del fotograma

        if puntos_faciales:
            puntos = puntos_faciales[0].landmark  # Obtiene los puntos faciales específicos
            for id, punto in enumerate(puntos[474:478]):  # Itera sobre los puntos faciales específicos
                x = int(punto.x * ancho_fotograma)  # Calcula la coordenada x en píxeles en el fotograma
                y = int(punto.y * alto_fotograma)  # Calcula la coordenada y en píxeles en el fotograma
                cv2.circle(frame, (x, y), 3, (0, 255, 0))  # Dibuja un círculo en el fotograma en la posición (x, y)
                if id == 1:
                    x_pantalla = ancho_pantalla / ancho_fotograma * x  # Calcula la coordenada x correspondiente en la pantalla
                    y_pantalla = alto_pantalla / alto_fotograma * y  # Calcula la coordenada y correspondiente en la pantalla
                    pyautogui.moveTo(x_pantalla, y_pantalla)  # Mueve el cursor del mouse a la posición (x_pantalla, y_pantalla)

            ojo_izquierdo = [puntos[145], puntos[159]]  # Obtiene los puntos faciales específicos para el ojo izquierdo
            for punto in ojo_izquierdo:
                x = int(punto.x * ancho_fotograma)  # Calcula la coordenada x en píxeles en el fotograma
                y = int(punto.y * alto_fotograma)  # Calcula la coordenada y en píxeles en el fotograma
                cv2.circle(frame, (x, y), 3, (0, 255, 255))  # Dibuja un círculo en el fotograma en la posición (x, y)

            if (ojo_izquierdo[0].y - ojo_izquierdo[1].y) < 0.008:  # Comprueba si el ojo izquierdo está cerrado (basado en las coordenadas y los puntos faciales)
                pyautogui.click()  # Realiza un clic con el cursor
                pyautogui.sleep(1)  # Espera 1 segundo

        cv2.imshow('Trackeo', frame)  # Muestra el fotograma con los puntos faciales y círculos dibujados
        if cv2.waitKey(1) == ord('q'):  # Espera hasta que se presione la tecla 'q' para salir
            break

    camara.release()  # Libera la cámara
    cv2.destroyAllWindows()  # Cierra todas las ventanas de OpenCV
