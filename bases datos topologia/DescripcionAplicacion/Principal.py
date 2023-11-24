import os
from pygame import *
from pygame.locals import *
from PIL import Image
from Clasematrix import Matrix
from Claseconjunto import Conjunto

def main():
    archivo = "ship.png"
    matriz = Matrix()
    matriz.crear(archivo)

    print("Ancho: {} x Alto: {}".format(matriz.ancho, matriz.alto))
    laMatriz = matriz.valor
    altoMatriz = matriz.alto
    anchoMatriz = matriz.ancho
    laOtraMatriz = laMatriz

    x, i, a = 0, 0, 0

    for y in range(altoMatriz):
        if i == 1:
            break

        for x in range(anchoMatriz):
            if i == 1:
                break

            print("x: {}, y: {}, alto: {}, ancho: {}".format(x, y, altoMatriz, anchoMatriz))  # Agregar esta línea

            if laOtraMatriz[y][x] == 1:
                conjunto = Conjunto()
                conjunto.contar(laMatriz, altoMatriz, anchoMatriz)
                print("Area en píxeles contados: {}".format(conjunto.numero))
                numero = conjunto.numero
                a, b = x, y
                conjunto.marcarBorde(archivo, laOtraMatriz, altoMatriz, anchoMatriz, a, b)
                centro, radio, area = conjunto.centro, conjunto.radio, conjunto.area
                laOtraMatriz = conjunto.valor

                if area == 0:
                    i = 1
                    print("Objeto no encontrado")
                else:
                    circularidad = min(area, numero) / max(area, numero)
                    a, b, i = x, y, 1
                    break
            elif laOtraMatriz[y][x] == 0:
                numero, radio, area, circularidad, centro = 0, 0, 0, 0, 0

    print("\nCARACTERISTICAS DEL OBJETO:")
    print("Coeficiente de circularidad: {:.2f}".format(circularidad))
    print("Coordenadas del Centro: {}".format(centro))
    print("Radio: {:.2f}".format(radio))
    print("Area calculada: {}".format(area))
    print(conjunto.contenido)

if __name__ == "__main__":
    main()
