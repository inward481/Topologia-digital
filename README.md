# Topologia-digital

**# Descripción**

Este proyecto es una implementación de la topología digital en Python. El objetivo es proporcionar una herramienta fácil de usar para comprender las definiciones de una manera didactica en python basandome en el articulo de **la topología digital y sus aplicaciones en la visión artificial.** de Jorge Alejandro Kamlofsky

**# Motivación**

La topología digital es una rama de la matemática que estudia el comportamiento de las formas en imágenes digitales. Es una herramienta esencial para la visión artificial, ya que se utiliza para analizar y clasificar objetos en imágenes, para detectar bordes y discontinuidades, y para segmentar imágenes.

**# Artículo**

El proyecto se basa en el artículo "Topología digital: base para la visión artificial" de Jorge Alejandro Kamlofsky. El artículo proporciona una introducción a la topología digital y sus aplicaciones en la visión artificial.

**# Instrucciones de uso**

Para empezar a usar el proyecto, sigue estos pasos:

1. Instala Python.
2. Clona el repositorio de GitHub.
3. Abre el archivo `main.py` en un editor de texto.
4. Modifica el código para cargar la imagen que quieres analizar.
5. Ejecuta el archivo `main.py`.

**# Funciones importantes**

Las siguientes funciones son importantes para el proyecto:

* **`graficarPlanoDigital(vecinos_punto_8N)`:** Esta función grafica un plano digital. La entrada es una lista de vecinos de un punto, y la salida es una imagen.
* **`vecindad(punto, tipo = "4N"):`:** Esta función devuelve la vecindad de un punto. La entrada es un punto y un tipo de vecindad, y la salida es una lista de puntos.
* **`componentes_conexas(S, tipo_trayectoria="4N"):`:** Esta función devuelve las componentes conexas de un conjunto. La entrada es un conjunto y un tipo de trayectoria, y la salida es una lista de conjuntos.

**# Código orientado a objetos**

El proyecto también incluye un código orientado a objetos que implementa las funciones mencionadas anteriormente. El código orientado a objetos es más modular y fácil de entender que el código procedural.

**# Aplicaciones**

El proyecto puede utilizarse para una variedad de aplicaciones en la visión artificial, como:

* **Análisis de objetos:** El proyecto puede utilizarse para analizar el contorno de objetos en imágenes.
* **Segmentación de imágenes:** El proyecto puede utilizarse para segmentar imágenes en componentes conexas.
* **OCR:** El proyecto puede utilizarse para aplicar ocr a imágenes.

**# Referencias**

* Kamlofsky, Jorge Alejandro. "Topología digital: base para la visión artificial." Tesis de Licenciatura en Matemática, Universidad Nacional de La Plata, 2011.
* https://www.datasmarts.net/como-aplicar-ocr-facilmente-con-easyocr/: https://www.datasmarts.net/como-aplicar-ocr-facilmente-con-easyocr/

**# Imágenes y documentos**

El proyecto incluye varias imágenes que se utilizan para ilustrar el funcionamiento de las funciones y clases implementadas. Estas imágenes se encuentran en las siguientes carpetas:

* **`cubo.png`:** Esta imagen representa un cubo.
* **`curva.png`:** Esta imagen representa una curva.
* **`DescripcionAplicacion`:** Esta carpeta contiene las imágenes utilizadas para ilustrar el código orientado a objetos(replica del codigo del articulo).
* **`exit.png`:** Esta imagen representa un botón de salida.
* **`muestraSangre.jpg`:** Esta imagen representa una muestra de sangre.
* **`OH.png`:** Esta imagen representa la letra "O".
* **`photoSebastian.jpeg`:** Esta imagen representa a Sebastián.
* **`puntosdelborde.txt`:** Este archivo contiene los puntos del borde de una imagen.
* **`recta.png`:** Esta imagen representa una recta.
* **`ship.png`:** Esta imagen representa un barco.
* **`TopologiaDigital.ipynb`:** Este archivo contiene un cuaderno de Jupyter que se utiliza para ilustrar el proyecto.
* **`TopologiaDigital.pdf`:** Este archivo contiene un documento PDF que se utiliza para ilustrar el proyecto.
* **`triangle.png`:** Esta imagen representa un triángulo.
* **`aplicacion.py`:** Codigo de https://www.datasmarts.net/como-aplicar-ocr-facilmente-con-easyocr/: https://www.datasmarts.net/como-aplicar-ocr-facilmente-con-easyocr/


**# Contacto**

Para obtener más información sobre el proyecto, póngase en contacto con Juan Sebastian Romeroa través de la siguiente dirección de correo electrónico:

```
juans.romerob@konradlorenz.edu.co
```

**# Problemas **

a la hora de ejecutar el codigo para la seccion de la replica del codigo que se encuentra en la carpeta DescripcionAplicacion tiene algunas fallas.
Hay un documento se debe intallar muchas librerias para que funcione correctamente, igualmente
agrego  un documento  llamado references.txt donde estan todas la librerias para intalar en ubuntu desde el bash: pip install -r requirements.txt y despues para ejecutar ir a la carpeta donde esta el .py y escribir: 
python aplicacion.py -i exit.png -l en,ar  en mi caso; python3 applicacion.py -i exit.png -l en
