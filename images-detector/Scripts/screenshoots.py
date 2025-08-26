import cv2 as cv
import numpy as np
from time import time
import pygetwindow as gw
import pyautogui
import win32gui
import win32ui
import win32con

class Screenshots:
    top = 0
    left = 0
    right = 0
    bottom = 0
    pantalla = None
    w = 0
    h = 0
    def __init__(self, titulo=None):
        if titulo is None:
            self.pantalla = win32gui.GetDesktopWindow()
            self.w, self.h = pyautogui.size()
        else:
            self.title = titulo
            ventana = gw.getWindowsWithTitle(titulo)
            ventana = ventana[0]
            self.w = ventana.width
            self.h = ventana.height
            self.pantalla = win32gui.FindWindow(None, self.title)





    def screenshot(self):

        pantallaDC = win32gui.GetWindowDC(self.pantalla)
        DCObjeto = win32ui.CreateDCFromHandle(pantallaDC)
        DCObjetoCompatible = DCObjeto.CreateCompatibleDC()
        BitMap = win32ui.CreateBitmap()
        BitMap.CreateCompatibleBitmap(DCObjeto, self.w, self.h)
        DCObjetoCompatible.SelectObject(BitMap)
        DCObjetoCompatible.BitBlt((0, 0), (self.w, self.h), DCObjeto, (16, 46), win32con.SRCCOPY)

        bmpStr = BitMap.GetBitmapBits(True)
        imagen = np.fromstring(bmpStr, dtype='uint8')
        imagen.shape = (self.h, self.w, 4)



        
        DCObjeto.DeleteDC()
        DCObjetoCompatible.DeleteDC()
        win32gui.ReleaseDC(self.pantalla, pantallaDC)
        win32gui.DeleteObject(BitMap.GetHandle())

        imagen = imagen[..., :3]

        imagen = np.ascontiguousarray(imagen)


        return imagen




