import cv2 as cv
import numpy as np
import os
from time import time
from screenshoots import Screenshots
from clickPoint import click


screen = Screenshots() #Importante, para que funcione se tiene que poner el titulo de la ventana a capturar, para grabar pantalla dejar vacio - Nota 2025
clickPoint = click("Nombre.jpg") # <- Imagen a buscar


looptime = time()
while (True):
    imagen = screen.screenshot()

    rectangles = clickPoint.clickPoints(imagen, 0.1, "rectangles")

    print('FPS: {}'.format(1 / (time() - looptime)))
    looptime = time()
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break