import sys
from lector_col import Lector_col
from clasificador import ClasificadorFiguras

def main():
    # 1. Validación de argumentos de entrada
    if len(sys.argv) < 2:
        print("Error: Argumentos insuficientes.")
        print("Uso correcto: python main.py <ruta_de_la_imagen.bmp>")
        sys.exit(1)

    ruta_imagen = sys.argv[1]

    # Validación visual (avisa al usuario si la extensión no es .bmp)
    if not ruta_imagen.lower().endswith('.bmp'):
        print("El archivo no termina en '.bmp'.")
        print("El programa intentará procesarlo, pero asegúrate de que el formato sea correcto.\n")

    try:
        print(f"Cargando imagen '{ruta_imagen}'...")
        
        # 2. Inicialización de clases y lectura de imagen
        lector = Lector_col(ruta_imagen)
        figuras_encontradas = lector.obtener_figuras()
        
        if not figuras_encontradas:
            print("ℹNo se encontraron figuras (la imagen es de un solo color).")
            sys.exit(0)
            
        print(f"Se encontraron {len(figuras_encontradas)} figura(s). Analizando...\n")
        
        # 3. Clasificación 
        clasificador = ClasificadorFiguras()
        
        print("-" * 50)
        print(f"{'Figura':<8} | {'Categoría':<20} | {'Color Hex'}")
        print("-" * 50)
        
        for idx, figura in enumerate(figuras_encontradas, start=1):
            # Extraer color y ejecutar algoritmo de clasificación
            color_hex = figura['color']
            categoria = clasificador.clasificar(figura['pixeles'])
            
            # Diccionario para imprimir un formato más legible
            nombres_cat = {
                'C': 'C (Cuadrilátero)',
                'T': 'T (Triángulo)',
                'O': 'O (Círculo)',
                'X': 'X (Otro)'
            }
            
            nombre_legible = nombres_cat.get(categoria, categoria)
            print(f"{idx:<8} | {nombre_legible:<20} | {color_hex}")
            
        print("-" * 50)

    # 4. Manejo de Errores Controlados
    except ValueError as ve:
        # Aquí capturamos el FileNotFoundError de lector
        print(f"\n Error de Archivo: {ve}")
        sys.exit(1)
    except Exception as e:
        # Evita que el programa arroje un "stack trace" críptico al usuario final
        print(f"\nError Inesperado del Sistema: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()