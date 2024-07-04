class Coche:
    def __init__(self, nombre, velocidad_maxima, aceleracion):
        self.nombre = nombre
        self.velocidad_maxima = velocidad_maxima
        self.aceleracion = aceleracion
        self.posicion = 0.0
        self.velocidad = 0.0
    
    def mover(self, tiempo):
        # Actualizar velocidad con aceleración
        self.velocidad += self.aceleracion * tiempo
        # Limitar velocidad a la velocidad máxima
        if self.velocidad > self.velocidad_maxima:
            self.velocidad = self.velocidad_maxima
        # Actualizar posición basada en la velocidad actual y el intervalo de tiempo
        self.posicion += self.velocidad * tiempo

class Carrera:
    def __init__(self):
        self.coches = []
    
    def agregar_coche(self, coche):
        self.coches.append(coche)
    
    def iniciar_carrera(self, duracion, intervalo):
        tiempo_actual = 0
        while tiempo_actual < duracion:
            for coche in self.coches:
                coche.mover(intervalo)
                print(f"{coche.nombre} - Posición: {round(coche.posicion, 1)}")
            tiempo_actual += intervalo
            print("---")
        
        # Determinar el ganador
        ganador = max(self.coches, key=lambda coche: coche.posicion)
        print(f"Ganador: {ganador.nombre}")

def main():
    # Crear instancias de coches
    coche1 = Coche("Coche 1", 200.0, 10.0)
    coche2 = Coche("Coche 2", 220.0, 8.0)
    coche3 = Coche("Coche 3", 210.0, 9.0)
    
    # Crear instancia de carrera
    carrera = Carrera()
    
    # Agregar coches a la carrera
    carrera.agregar_coche(coche1)
    carrera.agregar_coche(coche2)
    carrera.agregar_coche(coche3)
    
    # Iniciar carrera
    carrera.iniciar_carrera(10, 1)  # duración: 10 segundos, intervalo: 1 segundo

if __name__ == "__main__":
    main()
