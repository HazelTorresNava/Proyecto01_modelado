# Proyecto01_modelado
# Detector y Clasificador de Figuras Geométricas en Archivos `.BMP`

Este proyecto es una herramienta ejecutable desde la línea de comandos (CLI) capaz de procesar imágenes en formato `.bmp`, identificar figuras geométricas de colores sólidos sobre un fondo uniforme y clasificarlas por su categoría y color en formato hexadecimal.

## 👥 Datos Generales

* **Materia:** [Modelado]
* **Profesor/a:** [José Galaviz]
* **Ayudànte:** [Brenda Ayala Flores]

### Integrantes

* **Hazel Torres Nava** - [319158496 / hazelt@ciecnias.unam.mx]


## 🏷️ Categorías de Clasificación

| Código | Categoría     | Figuras Incluidas                                         |
| :----: | ------------- | --------------------------------------------------------- |
|  **C** | Cuadriláteros | Cuadrados, rectángulos, rombos, trapezoides               |
|  **T** | Triángulos    | Equiláteros, isósceles, escalenos, rectángulos            |
|  **O** | Círculos      | Formas circulares simétricas                              |
|  **X** | Otros         | Cualquier polígono o forma que no caiga en las anteriores |

## 📁 Estructura del Proyecto

```text
.
├── main.py            # Punto de entrada principal (CLI) y orquestador
├── lector_bmp.py      # Módulo de lectura, manejo de píxeles y segmentación por color (DFS)
├── clasificador.py    # Módulo de clasificación geométrica mediante análisis de perfil radial
├── generador.py       # Script auxiliar para generar el banco de imágenes de prueba
├── img/               # Directorio para almacenar las imágenes de prueba (.bmp)
└── README.md          # Instrucciones y datos generales del repositorio
```

## ⚙️ Requisitos e Instalación

* **Python 3.8 o superior**
* **Pillow (PIL):** Requerida únicamente para ejecutar el script `generador.py`, que crea las imágenes de prueba.

### Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

2. Instalar la dependencia necesaria para el generador de pruebas:

```bash
pip install pillow
```

## 🚀 Guía de Uso

### 1. Generar el banco de pruebas

Para crear automáticamente las imágenes `.bmp` de prueba en la carpeta `img/`, ejecuta:

```bash
python generador.py
```

### 2. Clasificar una imagen

Ejecuta `main.py` pasando la ruta del archivo `.bmp` como parámetro desde la terminal.

#### Ejemplo con una sola figura

```bash
python main.py img/prueba_01_cuadrado.bmp
```

#### Ejemplo con múltiples figuras en la misma imagen

```bash
python main.py img/prueba_10_multiforma.bmp
```

## 📊 Ejemplo de Salida

```text
Cargando imagen 'img/prueba_10_multiforma.bmp'...
✅ Se encontraron 3 figura(s). Analizando...

--------------------------------------------------
Figura   | Categoría            | Color Hex
--------------------------------------------------
1        | C (Cuadrilátero)     | #FF0000
2        | O (Círculo)          | #00FF00
3        | T (Triángulo)        | #0000FF
--------------------------------------------------
```

