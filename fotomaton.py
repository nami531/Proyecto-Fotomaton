import cv2
import os
import time
from Camara import Camara
from Imagen import Imagen

dimensiones = (2560, 1080)#ancho alto
cam = Camara(dimensiones)
img = Imagen("foto.jpg")

foto = False
while not foto:
    # Se comprueba que se obtiene imagen
    ret, frame = cam.leer()

    if ret == False:
        raise Exception ("No se ha podido obtener ninguna imagen de la camara")

    img.mostrar(frame)

    # Si se presiona la tecla de esc se guardará la foto, esto se deberá reemplazar con pygame
    if cv2.waitKey(1) == 27:
        img.guardar(frame)
        time.sleep(5)
        respuesta = input("¿Te gusta la imagen? s|n: ")
        if respuesta.lower() == "s":
            # se tendría que poner el comando de la impresora
            # os.startfile(nombre_archivo, "print") o hacer un script :/
            foto = True
        else:
            img.borrar()

cam.finalizar()
img.borrar()