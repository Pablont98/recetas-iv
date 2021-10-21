from Ingrediente import Ingrediente

class Receta:
    '''Clase que alberga los datos necesarios para guardar una receta correctamente.'''
    
    def __init__(self, nombre, ingredientes, duracion, dificultad, elaboracion):
        self.nombre = nombre
        self.ingredientes = list(ingredientes)
        self.duracion = duracion
        self.dificultad = dificultad
        self.elaboracion = elaboracion

    '''Método que calcula el aporte calórico total de la receta a partir de sus ingredientes.'''
    
    def kcals_maximas(self):
            kcals = 0
            for ing in self.ingredientes:
                kcals += ing.kcals
            return kcals
