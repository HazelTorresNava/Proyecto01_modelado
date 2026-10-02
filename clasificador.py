import math

class ClasificadorFiguras:
    def clasificar(self, pixeles):
        if not pixeles:
            return 'X'
        
        # 1. Calcular el centroide (centro de masa)
        cx = sum(p[0] for p in pixeles) / len(pixeles)
        cy = sum(p[1] for p in pixeles) / len(pixeles)
        
        # 2. Extraer el contorno (píxeles que tocan el fondo)
        # Usamos un Set para que las búsquedas sean O(1)
        pixeles_set = set(pixeles)
        contorno = []
        for x, y in pixeles:
            # Si al menos un vecino ortogonal NO pertenece a la figura, entonces es un borde
            if (x-1, y) not in pixeles_set or (x+1, y) not in pixeles_set or \
               (x, y-1) not in pixeles_set or (x, y+1) not in pixeles_set:
                contorno.append((x, y))
                
        if not contorno:
            return 'X'
        
        # 3. Calcular distancias del centroide al contorno (Radios)
        distancias = []
        for x, y in contorno:
            dist = math.hypot(x - cx, y - cy)
            distancias.append(dist)
            
        radio_promedio = sum(distancias) / len(distancias)
        
        # Calcular desviación estándar (qué tanto varían las distancias)
        varianza = sum((d - radio_promedio)**2 for d in distancias) / len(distancias)
        desviacion = math.sqrt(varianza)
        
        # 4. Detectar Círculo (O)
        # Un círculo perfecto tiene desviación 0. con humbral de 12% para tolerancia a píxeles
        if radio_promedio > 0 and (desviacion / radio_promedio) < 0.12:
            return 'O'
            
        # 5. Encontrar vértices mediante el Perfil Radial
        # Dividimos los 360 grados en 72 "rebanadas" de 5 grados cada una
        rebanadas = 72
        perfil = [0] * rebanadas
        
        for x, y in contorno:
            dist = math.hypot(x - cx, y - cy)
            # atan2 da el ángulo. Lo convertimos a grados (0-360)
            angulo = math.degrees(math.atan2(y - cy, x - cx)) % 360
            indice = int(angulo / (360 / rebanadas))
            
            # Guardamos la distancia más larga en esa rebanada
            if dist > perfil[indice]:
                perfil[indice] = dist
                
        # Rellenar posibles huecos en blanco copiando el vecino (por si una rebanada quedó vacía)
        for i in range(rebanadas):
            if perfil[i] == 0:
                perfil[i] = perfil[(i-1) % rebanadas]
                
        # Suavizar el perfil (Media móvil) para ignorar "escalones" generados por los píxeles
        perfil_suave = [0] * rebanadas
        for i in range(rebanadas):
            previo = perfil[(i-1) % rebanadas]
            actual = perfil[i]
            siguiente = perfil[(i+1) % rebanadas]
            perfil_suave[i] = (previo + actual + siguiente) / 3
            
        # 6. Contar vértices (picos locales)
        picos = 0
        for i in range(rebanadas):
            actual = perfil_suave[i]
            previo = perfil_suave[(i-1) % rebanadas]
            siguiente = perfil_suave[(i+1) % rebanadas]
            
            # Es un pico si es mayor que sus vecinos y sobresale del promedio
            if actual > previo and actual > siguiente:
                # Solo contamos picos que sobresalgan al menos un 5% del radio promedio
                if actual > (radio_promedio * 1.05):
                    picos += 1
                    
        # 7. Retornar la clasificación
        if picos == 3:
            return 'T' # Triángulo
        elif picos == 4:
            return 'C' # Cuadrilátero (Cuadrado, Rectángulo, Rombo, Trapecio)
        else:
            return 'X' # Cualquier otra cosa