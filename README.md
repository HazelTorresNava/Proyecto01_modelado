# Proyecto01_modelado

## 👥 Datos Generales

* **Materia:** [Modelado]
* **Profesor/a:** [José Galaviz]
* **Ayudànte:** [Brenda Ayala Flores]

### Integrantes

* **Hazel Torres Nava** - [319158496 / hazelt@ciecnias.unam.mx]

# Detector y Clasificador de Figuras Geométricas

Este proyecto es una herramienta de línea de comandos (CLI) desarrollada en Python que analiza imágenes en formato `.bmp` para detectar figuras geométricas de colores sólidos sobre un fondo uniforme. Identifica cada figura agrupando sus píxeles contiguos y reporta su color en formato hexadecimal junto con su categoría geométrica.

## 📁 Estructura del Proyecto

El repositorio está organizado de la siguiente manera:

```text
.
├── main.py            # Archivo principal y orquestador del programa
├── lector_col.py      # Lectura de imágenes y agrupación de píxeles por color
├── clasificador.py    # Clasificación geométrica mediante perfiles radiales
├── img/
│   └── generador.py   # Generador automático de imágenes de prueba
└── README.md          # Documentación del proyecto
```

### Descripción de los archivos

* `main.py`: Archivo principal que recibe los argumentos de la consola, valida la extensión del archivo y orquesta la clasificación.
* `lector_col.py`: Módulo encargado de leer la imagen, manejar posibles errores de archivo y agrupar los píxeles por color usando un algoritmo iterativo con una pila (DFS).
* `clasificador.py`: Algoritmo matemático que extrae el contorno de los píxeles, calcula el centroide y utiliza perfiles radiales divididos en 72 rebanadas para clasificar la geometría.
* `img/`: Directorio donde se almacenan las imágenes de prueba.

  * `generador.py`: Script que utiliza la librería Pillow (PIL) para dibujar y guardar 10 imágenes `.bmp` de prueba de forma automática.

## ⚙️ Requisitos Previos

Para ejecutar el programa base no se requieren librerías externas pesadas. Sin embargo, para generar el banco de imágenes de prueba es necesario instalar `Pillow`.

```bash
pip install Pillow
```

## 🚀 Guía de Uso

### 1. Generar el banco de imágenes de prueba

El script generador se encuentra dentro de la carpeta `img`, por lo que debe ejecutarse desde ese directorio para que las imágenes se guarden correctamente en la misma ubicación:

```bash
cd img
python generador.py
cd ..
```

Esto creará archivos `.bmp` como:

* `prueba_01_cuadrado.bmp`
* `prueba_07_circulo.bmp`
* `prueba_10_multiforma.bmp`

Estos archivos quedan listos para ser analizados por el clasificador.

### 2. Analizar una imagen

Para procesar una imagen, se ejecuta `main.py` pasando como argumento la ruta relativa del archivo `.bmp`:

```bash
python main.py img/prueba_10_multiforma.bmp
```

## 🏷️ Categorías de Clasificación

El sistema analiza los vértices y la desviación estándar de la figura para clasificarla en una de las siguientes cuatro categorías:

| Código | Categoría    | Criterio                                                      |
| :----: | ------------ | ------------------------------------------------------------- |
|  **C** | Cuadrilátero | La figura presenta 4 picos sobresalientes en su contorno.     |
|  **T** | Triángulo    | La figura presenta exactamente 3 picos en su perfil radial.   |
|  **O** | Círculo      | La desviación del radio respecto al promedio es menor al 12%. |
|  **X** | Otro         | Figura irregular que no cumple con los criterios anteriores.  |

## 📊 Ejemplo de Salida

Al ejecutar correctamente el clasificador, la terminal devuelve un reporte en forma de tabla:

```text
Cargando imagen 'img/prueba_10_multiforma.bmp'...
Se encontraron 3 figura(s). Analizando...

--------------------------------------------------
Figura   | Categoría            | Color Hex
--------------------------------------------------
1        | C (Cuadrilátero)     | #FF0000
2        | O (Círculo)          | #00FF00
3        | T (Triángulo)        | #0000FF
--------------------------------------------------
```

