from PIL import Image, ImageDraw

def crear_imagen_prueba(nombre_archivo, color_fondo, instrucciones_dibujo):
    """
    crea una imagen BMP de prueba con un color de fondo y varias figuras geométricas.
    """
    # Crear imagen con color de fondo
    img = Image.new("RGB", (200, 200), color=color_fondo)
    draw = ImageDraw.Draw(img)
    
    # Ejecutar las instrucciones de dibujo
    for forma, coords, color in instrucciones_dibujo:
        if forma == "poligono":
            draw.polygon(coords, fill=color)
        elif forma == "elipse":
            draw.ellipse(coords, fill=color)
            
    # Guardar sin compresión para asegurar que es un BMP puro
    img.save(nombre_archivo)
    print(f"Generada: {nombre_archivo}")

def generar_banco_pruebas():
    print("Generando banco de imágenes de prueba...")

    # 1. Cuadrado (C)
    crear_imagen_prueba("prueba_01_cuadrado.bmp", "#FFFFFF", [
        ("poligono", [(50, 50), (150, 50), (150, 150), (50, 150)], "#FF0000")
    ])

    # 2. Rectángulo (C)
    crear_imagen_prueba("prueba_02_rectangulo.bmp", "#CCCCCC", [
        ("poligono", [(20, 80), (180, 80), (180, 120), (20, 120)], "#0000FF")
    ])

    # 3. Rombo (C)
    crear_imagen_prueba("prueba_03_rombo.bmp", "#000000", [
        ("poligono", [(100, 20), (180, 100), (100, 180), (20, 100)], "#00FF00")
    ])

    # 4. Trapecio (C)
    crear_imagen_prueba("prueba_04_trapecio.bmp", "#FFFFFF", [
        ("poligono", [(60, 50), (140, 50), (180, 150), (20, 150)], "#FFA500")
    ])

    # 5. Triángulo Rectángulo (T)
    crear_imagen_prueba("prueba_05_triangulo_rect.bmp", "#EEEEEE", [
        ("poligono", [(40, 40), (40, 160), (160, 160)], "#800080")
    ])

    # 6. Triángulo Isósceles (T)
    crear_imagen_prueba("prueba_06_triangulo_iso.bmp", "#333333", [
        ("poligono", [(100, 30), (170, 160), (30, 160)], "#FFFF00")
    ])

    # 7. Círculo (O)
    crear_imagen_prueba("prueba_07_circulo.bmp", "#FFFFFF", [
        ("elipse", [(50, 50), (150, 150)], "#00FFFF")
    ])

    # 8. Pentágono (X - Otro)
    crear_imagen_prueba("prueba_08_pentagono.bmp", "#AAAAAA", [
        ("poligono", [(100, 20), (180, 70), (150, 160), (50, 160), (20, 70)], "#FF1493")
    ])

    # 9. Figura Irregular (X - Otro)
    crear_imagen_prueba("prueba_09_irregular.bmp", "#FFFFFF", [
        ("poligono", [(80, 20), (120, 40), (180, 100), (130, 180), (40, 150), (20, 80)], "#8B4513")
    ])

    # 10. Múltiples figuras (Prueba de segmentación)
    crear_imagen_prueba("prueba_10_multiforma.bmp", "#222222", [
        ("poligono", [(20, 20), (80, 20), (80, 80), (20, 80)], "#FF0000"),  # Cuadrado C
        ("elipse", [(110, 110), (170, 170)], "#00FF00"),                    # Círculo O
        ("poligono", [(150, 20), (180, 80), (120, 80)], "#0000FF")          # Triángulo T
    ])

    print("¡10 imágenes generadas con éxito!")

if __name__ == "__main__":
    generar_banco_pruebas()