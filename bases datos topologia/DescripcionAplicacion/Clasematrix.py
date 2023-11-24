import os
from PIL import Image
import math

class Matrix(object):
    """La clase Matrix carga una imagen y devuelve una matriz binaria segmentada"""

    def __init__(self):
        self.__valor = 0
        self.__alto = 0
        self.__ancho = 0

    def getValor(self):
        return self.__valor

    def getAlto(self):
        return self.__alto

    def getAncho(self):
        return self.__ancho

    def setValor(self, valor):
        self.__valor = valor

    def setAlto(self, alto):
        self.__alto = alto

    def setAncho(self, ancho):
        self.__ancho = ancho

    valor = property(getValor, setValor)
    alto = property(getAlto, setAlto)
    ancho = property(getAncho, setAncho)

    def crear(self, archivo):
        """Toma el archivo de imagen y retorna los valores de ancho y alto"""
        """Con ancho y alto, segmenta y pasa 1 y 0 a una matriz segmentada"""
        imagen = Image.open(archivo)
        alto = imagen.size[1]  # toma el Alto
        ancho = imagen.size[0]  # toma el ancho
        self.__ancho = ancho
        self.__alto = alto
        print(str(alto) + " x " + str(ancho))
        x = 0
        y = 0
        # Aquí se introducen los valores RGB que segmentan por el color anaranjado.
        Rmin = 92
        Rmax = 224
        Gmin = 68
        Gmax = 128
        Bmin = 50
        Bmax = 101
        valor = []
        for y in range(alto):
            a = [0] * ancho
            valor.append(a)
        for y in range(0, alto):
            for x in range(0, ancho):
                R = imagen.getpixel((x, y))[0]
                G = imagen.getpixel((x, y))[1]
                B = imagen.getpixel((x, y))[2]
                if ((R < Rmax and R >= Rmin) and (G < Gmax and G >= Gmin) and (B <= Bmax and B > Bmin)):
                    valor[y][x] = 1
                else:
                    valor[y][x] = 0
        print("Lectura de imagen terminada")
        self.__valor = valor
        return self.__valor, self.__ancho, self.__alto
