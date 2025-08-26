import cv2 as cv
import numpy as np
import os
from time import time
from screenshoots import Screenshots
from clickPoint import click


screen = Screenshots() #Important, to make it works you need to put the window's title to capture them, if want to record the screen let a blank space- Nota 2025
clickPoint = click("Nombre.jpg") # <- image to search


looptime = time()
while (True):
    imagen = screen.screenshot()

    rectangles = clickPoint.clickPoints(imagen, 0.1, "rectangles")

    print('FPS: {}'.format(1 / (time() - looptime)))
    looptime = time()
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break