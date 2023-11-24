import os
import pygame
from PIL import Image
import math
from Clasematrix import Matrix

class Conjunto(object):
    """Divide a la matriz en conjuntos segmentados conexos"""

    def __init__(self):
        self.__area = 1
        self.__alto = 0
        self.__centro = 0
        self.__ancho = 0
        self.__circularidad = 0
        self.__numero = 0
        self.__valor = 0
        self.__contenido = 0
        self.__centro = 0
        self.__radio = 0

    def getArea(self):
        return self.__area

    def getAlto(self):
        return self.__alto

    def getAncho(self):
        return self.__ancho

    def getCircularidad(self):
        return self.__circularidad

    def getNumero(self):
        return self.__numero

    def getContenido(self):
        return self.__contenido

    def getValor(self):
        return self.__valor

    def getCentro(self):
        return self.__centro

    def getRadio(self):
        return self.__radio

    def setArea(self, area):
        self.__valor = area

    def setAlto(self, alto):
        self.__alto = alto

    def setAncho(self, ancho):
        self.__ancho = ancho

    def setCircularidad(self, circularidad):
        self.__circularidad = circularidad

    def setNumero(self, numero):
        self.__numero = numero

    def setContenido(self, contenido):
        self.__contenido = contenido

    def setValor(self, valor):
        self.__valor = valor

    def setCentro(self, centro):
        self.__centro = centro

    def setRadio(self, radio):
        self.__radio = radio

    area = property(getArea, setArea)
    alto = property(getAlto, setAlto)
    ancho = property(getAncho, setAncho)
    numero = property(getNumero, setNumero)
    circularidad = property(getCircularidad, setCircularidad)
    contenido = property(getContenido, setContenido)
    valor = property(getValor, setValor)
    centro = property(getCentro, setCentro)
    radio = property(getRadio, setRadio)

    def contar(self, laMatriz, altoMatriz, anchoMatriz):
        """Cuenta la cantidad de píxeles que cumplen con la segmentación"""
        x = 0
        y = 0
        numero = 0
        a = 0

        for y in range(0, altoMatriz):
            for x in range(0, anchoMatriz):
                if laMatriz[x][y] == 0:
                    a = a + 1
                elif laMatriz[x][y] == 1:
                    numero = numero + 1

        self.__numero = numero
        return self.__numero

    def marcarBorde(self, archivo, laOtraMatriz, altoMatriz, anchoMatriz, a, b):
        """Se pone una marca a los elementos que pertenecen al borde"""
        imagen = Image.open(archivo)
        MaxX = 0
        MinX = anchoMatriz
        MaxY = 0
        MinY = anchoMatriz

        V8No = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        V8N = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

        p = [0] * 2
        q = [0] * 2
        a1 = [0] * 2
        b1 = [0] * 2
        i = 1
        p = [a, b]
        q = [a, b - 1]

        P = [p]
        Q = [q]

        laOtraMatriz[P[0][0]][P[0][1]] = 2
        laOtraMatriz[Q[0][0]][Q[0][1]] = -1

        Po = [p]
        Qo = [q]
        A = [a1]
        B = [b1]

        Base = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]

        k = 0
        pos = 0

        archivo_puntos = open('puntosdelborde.txt', 'w')
        archivo_puntos.writelines("[" + str(P[0][0]) + "," + str(P[0][1]) + "]" + "\n")

        imagen.putpixel((P[0][0], P[0][1]), (0, 0, 0))
        imagen.putpixel((Q[0][0], Q[0][1]), (255, 255, 255))

        while ((0 <= P[0][0] < altoMatriz) and (0 <= P[0][1] < anchoMatriz) and
               (0 <= Q[0][0] < altoMatriz) and (0 <= Q[0][1] < anchoMatriz) and
               (laOtraMatriz[P[0][0]][P[0][1]] == 1) and (laOtraMatriz[Q[0][0]][Q[0][1]] == 0) or
               (laOtraMatriz[Q[0][0]][Q[0][1]] == -1)):

            k = 0
            pos = 0

            if P[0][0] > MaxX:
                MaxX = P[0][0]
            else:
                n = 1

            if P[0][0] < MinX:
                MinX = P[0][0]
            else:
                n = 1

            if P[0][1] > MaxY:
                MaxY = P[0][1]
            else:
                n = 1

            if P[0][1] < MinY:
                MinY = P[0][1]
            else:
                n = 1

            laOtraMatriz[P[0][0]][P[0][1]] = 2
            laOtraMatriz[Q[0][0]][Q[0][1]] = -1

            for j in range(0, 8):
                for i in range(0, 2):
                    V8No[j][i] = Base[j][i] + P[0][i]

            B[0][0] = Q[0][0] - P[0][0]
            B[0][1] = Q[0][1] - P[0][1]

            for j in range(0, 8):
                if (B[0][0] == Base[j][0]) and (B[0][1] == Base[j][1]):
                    break
                pos = j

            for j in range(0, 8):
                if pos + j < 8:
                    for i in range(0, 2):
                        V8N[j][i] = V8No[pos + j][i]
                else:
                    for i in range(0, 2):
                        V8N[j][i] = V8No[pos + j - 8][i]

            k = 0

            for j in range(0, 8):
                if k == 1:
                    break

                for i in range(0, 2):
                    P[0][0] = V8N[j][0]
                    P[0][1] = V8N[j][1]

                    if laOtraMatriz[P[0][0]][P[0][1]] == 1:
                        Q[0][0] = V8N[j - 1][0]
                        Q[0][1] = V8N[j - 1][1]
                        k = 1
                        break

            archivo_puntos.writelines("[" + str(P[0][0]) + "," + str(P[0][1]) + "]" + "\n")

            imagen.putpixel((P[0][0], P[0][1]), (0, 0, 0))
            imagen.putpixel((Q[0][0], Q[0][1]), (255, 255, 255))

        archivo_puntos.close()
        imagen.save("bordemarcado.jpg")

        centro = [(MaxX + MinX) / 2, (MaxY + MinY) / 2]
        radio = float((((MaxX - ((MaxX + MinX) / 2)) + ((MaxX + MinX) / 2) - MinX + (MaxY - ((MaxY + MinY) / 2)) +
                        ((MaxY + MinY) / 2) - MinY)) / 4)
        area = 3.141 * (radio ** 2)

        self.__radio = radio
        self.__area = area
        self.__centro = centro
        self.__valor = laOtraMatriz
        self.__contenido = "Máx en X: " + str(MaxX) + " - Min en X: " + str(MinX) + " - Máx en Y: " + str(MaxY) + " - Min en Y: " + str(MinY)

        return self.__contenido, self.__valor, self.__centro, self.__area, self.__radio
