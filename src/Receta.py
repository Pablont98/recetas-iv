#Realizado por Pablo Nuñez Tejero
#Clase de prueba para realizar el objetivo 3 (no sirve para el objetivo 2)
#A espera de la version valida por parte de mi compeñero

class Receta:
    def __init__(self, nombre, ingredientes, duracion, dificultad, explicacion):
        self.nombre = nombre
        self.ingredientes = list(ingredientes)
        self.duracion = duracion
        self.dificultad = dificultad
        self.explicacion = explicacion

    #Metodo que calcula el total de calorias de la receta a partir de la lista de ingredientes
    def calcular_aporte_calorico_maximo(self):
        pass
