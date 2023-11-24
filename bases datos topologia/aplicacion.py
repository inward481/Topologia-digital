# Importamos las dependencias del script.
from argparse import ArgumentParser

import cv2
from easyocr import Reader

# Función que elimina los caracteres no ASCII del texto de entrada.
def cleanup_text(text):
    return ''.join([c if ord(c) < 128 else '' for c in text]).strip()

#Definimos los parámetros de entrada.
argument_parser = ArgumentParser()
argument_parser.add_argument('-i', '--image', required=True, help='exit.png')
argument_parser.add_argument('-l', '--langs', type=str, default='en',
                             help='Lista separada por comas de lenguajes a usar durante el OCR.')
arguments = vars(argument_parser.parse_args())

# Imprimimos los lenguajes con los que el programa va a trabajar.
languages = arguments['langs'].split(',')
print(f'Aplicando OCR con estos lenguajes: {languages}')

# Leemos la imagen de entrada.s
image = cv2.imread(arguments['image'])
cv2.imshow('Imagen', image)
cv2.waitKey(0)

# Aplicamos OCR utilizando los lenguajes definidos anteriormente.
reader = Reader(languages,use_nnpack=False, gpu=False)
results = reader.readtext(image)

# Iteramos sobre las predicciones del modelo de EasyOCR.
for bounding_box, text, probability in results:
    # Imprimimos la probabilidad del texto.
    print(f'{probability:.4f}: {text}')

    # Extraemos y ajustamos las coordenadas de la detección.
    tl, tr, br, bl = bounding_box
    tl = (int(tl[0]), int(tl[1]))
    tr = (int(tr[0]), int(tr[1]))
    br = (int(br[0]), int(br[1]))
    bl = (int(bl[0]), int(bl[1]))

    # Limpiamos el texto, y lo mostramos en la imagen.
    text = cleanup_text(text)
    cv2.rectangle(image, tl, br, (0, 255, 0), 2)
    cv2.putText(image, text, (tl[0], tl[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, .8, (0, 255, 0), 2)

# Mostramos el resultado en pantalla.
cv2.imshow('Resultado', image)
cv2.waitKey(0)

# Destruimos las ventanas creadas.
cv2.destroyAllWindows()