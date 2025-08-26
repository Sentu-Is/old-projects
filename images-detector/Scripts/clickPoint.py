import cv2 as cv
import numpy as np


class click:
    imgBuscar = None
    objAncho = 0
    objAlto = 0
    metodo = None

    def __init__(self, imgBuscarPath, method=cv.TM_SQDIFF_NORMED):
        self.imgBuscar = cv.imread(imgBuscarPath, cv.IMREAD_UNCHANGED)
        # Valor de ancho y alto del objeto
        self.objAncho = self.imgBuscar.shape[1]
        self.objAlto = self.imgBuscar.shape[0]
        self.metodo = method

    def clickPoints(self,imgOriginal,threshold=0.5,debugMode=None):

        # Buscador de imagenes

        result = cv.matchTemplate(imgOriginal, self.imgBuscar, self.metodo)

        # Establecer valores de las imagenes buscadas (Presicion de parecido con la original y localizacion)

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        print("mejor match en: ", str(max_loc))
        print("su valor es: ", max_val)

        # Junta los resultados de un array 3d a un array doble donde se puede procesar mejor
        loc = np.where(result <= threshold)
        loc = list(zip(*loc[::-1]))

        # crear lista de rectangulos
        rectangles = []
        for locations in loc:
            rect = [int(locations[0]), int(locations[1]), self.objAncho, self.objAlto]
            rectangles.append(rect)
            rectangles.append(rect)

        # Agrupar los rectangulos, el primer parametro siempre es 1, en raros casos es 2 o 3,
        # el 2do parametro es la distancia en la que los rectangulos se van a juntar

        rectangles, ancho = cv.groupRectangles(rectangles, 1, 0.5)



        points = []


        # Rectangulear las imagenes
        if len(rectangles):
            print("Objeto encontrado", loc)

            lineColor = (0, 255, 0)
            lineType = cv.LINE_4
            markerColor = (255, 0, 0)
            markerType = cv.MARKER_CROSS


            # x Alto y. Largo. Ubicacion del objeto. W ancho. H largo tamaño del objeto
            for (x, y, w, h) in rectangles:

                centroY = y + int(w / 2)
                centroX = x + int(w / 2)

                points.append((centroX, centroY))

                if debugMode == "rectangles":
                    top_left = x, y
                    buttom_right = x + w, y + h

                    cv.rectangle(imgOriginal, top_left, buttom_right, color=lineColor, lineType=lineType)
                elif debugMode == "points":
                    cv.drawMarker(imgOriginal, (centroX, centroY), color=markerColor, markerType=markerType)
        if debugMode:
            cv.imshow("match", imgOriginal)
        return points
