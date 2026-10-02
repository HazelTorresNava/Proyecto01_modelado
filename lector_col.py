from PIL import Image

class Lector_col:
    """Clase para leer y analizar colores de una imagen BMP."""

    def __init__(self, ruta_archivo ):
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
        
    def rgb_a_hex(self, color_rgb):
        """Convierte una tupla (R, G, B) a formato hexadecimal."""
        return "#{:02X}{:02X}{:02X}".format(color_rgb[0], color_rgb[1], color_rgb[2])

    def obtener_figuras(self):
        """
        Recorre la imagen y agrupa los píxeles adyacentes del mismo color.
        Retorna una lista de diccionarios con el color y las coordenadas de la figura.
        """
        # Asumimos que el pixel de la esquina superior izquierda [0,0] es el fondo
        color_fondo = self.pixeles[0, 0]
        visitados = set()
        figuras = []

        for x in range(self.ancho):
            for y in range(self.alto):
                color_actual = self.pixeles[x, y]
                
                # Si el pixel no es el fondo y no ha sido procesado, encontramos una nueva figura
                if color_actual != color_fondo and (x, y) not in visitados:
                    pixeles_figura = []
                    pila = [(x, y)] # Usamos una pila (DFS) en lugar de recursión para evitar StackOverflow
                    
                    while pila:
                        cx, cy = pila.pop()
                        
                        if (cx, cy) in visitados:
                            continue
                            
                        visitados.add((cx, cy))
                        pixeles_figura.append((cx, cy))
                        
                        # Revisar vecinos ortogonales (Arriba, Abajo, Izquierda, Derecha)
                        vecinos = [(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)]
                        for vx, vy in vecinos:
                            # Validar que el vecino esté dentro de los límites de la imagen
                            if 0 <= vx < self.ancho and 0 <= vy < self.alto:
                                if (vx, vy) not in visitados and self.pixeles[vx, vy] == color_actual:
                                    pila.append((vx, vy))
                    
                    # Guardar la figura encontrada
                    figuras.append({
                        'color': self.rgb_a_hex(color_actual),
                        'pixeles': pixeles_figura
                    })
                    
        return figuras