#from Ingrediente import *

class Receta:
    '''Clase que alberga los datos necesarios para guardar una receta correctamente.'''

    def __init__(self, nombre, ingredientes, duracion, dificultad, elaboracion):
        self.nombre = nombre
        self.ingredientes = list(ingredientes)
        self.duracion = duracion
        self.dificultad = dificultad
        self.elaboracion = elaboracion

    def kcals_maximas(self):
        '''Método que calcula el aporte calórico total de la receta a partir de sus ingredientes.'''
        kcals_max = 0
        for ing in self.ingredientes:
            kcals_max += ing.kcals_totales()
        return kcals_max

    def visualizar_receta(self):
        '''Método que muestra una carta mostrando informacion referente a la receta'''
        string_ingredientes = ""
        for ingrediente in self.ingredientes:
            string_ingredientes += ingrediente.nombre + " cantidad: " + str(ingrediente.cantidad) + " " + ingrediente.unidad + "\n"

        string_dura_dificult = "\nDuracion: "+str(self.duracion)+" mins\n"+"\Dificultad: "+self.dificultad
        string_elaboracion = "\nElaboracion \n" + self.elaboracion
        carta_receta = (self.nombre + "\n\n" + string_ingredientes + string_dura_dificult + string_elaboracion)

        print(carta_receta)
