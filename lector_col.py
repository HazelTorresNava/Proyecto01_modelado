from PIL import Image

class Lector_col:
    """Clase para leer y analizar colores de una imagen BMP."""

    def __init__(self, ruta_archivo):
        """Inicializa el lector de color con la ruta del archivo BMP."""
        self.ruta = ruta_archivo
        
        # Cumpliendo con requisitos no funcionales: Manejo de errores claro
        try:
            self.imagen = Image.open(ruta_archivo).convert('RGB')
            self.ancho, self.alto = self.imagen.size
            self.pixeles = self.imagen.load()
        except FileNotFoundError:
            raise ValueError(f"Error: No se encontró el archivo en la ruta '{ruta_archivo}'. Verifica que el nombre sea correcto.")
        except Exception:
            raise ValueError(f"Error: El archivo '{ruta_archivo}' no es una imagen válida o está dañado.")