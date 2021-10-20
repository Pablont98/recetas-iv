from Ingrediente import Ingrediente


class Receta:
    '''Clase que alberga los datos necesarios para guardar una receta correctamente.'''
    nombre = ''
    ingredientes = Ingrediente()
    duracion = 0
    dificultad = 0
    elaboracion = ''
    kcals = 0

    def __init__(self, nombre, ingredientes, duracion, dificultad, elaboracion, kcals):
        self.nombre = nombre
        self.ingredientes = list(ingredientes)
        self.duracion = duracion
        self.dificultad = dificultad
        self.elaboracion = elaboracion
        self.kcals = kcals