from Ingrediente import Ingrediente

class Receta:
    '''Clase que alberga los datos necesarios para guardar una receta correctamente.'''
    
    def __init__(self, nombre, ingredientes, duracion, dificultad, elaboracion):
        self.nombre = nombre
        self.ingredientes = list(ingredientes)
        self.duracion = duracion
        self.dificultad = dificultad
        self.elaboracion = elaboracion

    def kcals_maximas(self):
        ''' Método que calcula el aporte calórico total de la receta a partir de sus ingredientes.'''
        kcals_max = 0
        for ing in self.ingredientes:
            if ((ing.nombre.find("Aceite") >= 0) and (ing.cantidad > 10)):
                kcals_max += ((10 * ing.kcals_totales())/100)
            else:
                kcals_max += ing.kcals_totales()
        return round(kcals_max,2)

    def hidratos_maximos(self):
        ''' Método que calcula el número de hidratos de la receta a partir de sus ingredientes.'''
        hidratos_max = 0
        for ing in self.ingredientes:
            hidratos_max += ing.hidratos_totales()
        return round(hidratos_max,2)

    def proteinas_maximas(self):
        ''' Método que calcula el número de proteinas de la receta a partir de sus ingredientes.'''
        proteinas_max = 0
        for ing in self.ingredientes:
            proteinas_max += ing.proteinas_totales()
        return round(proteinas_max,2)

    def grasas_maximas(self):
        ''' Método que calcula las grasas totales de la receta a partir de sus ingredientes.'''
        grasas_max = 0
        for ing in self.ingredientes:
            if (ing.nombre.find('Aceite')) and ing.cantidad > 10:
                grasas_max += (10 * ing.grasas_totales())/100
            grasas_max += ing.grasas_totales()
        return round(grasas_max,2)

    def visualizar_receta(self):
        '''Método que muestra una carta mostrando informacion referente a la receta'''
        string_ingredientes = ""
        for ingrediente in self.ingredientes:
            string_ingredientes += ingrediente.nombre + " cantidad: " + str(ingrediente.cantidad) + " " + ingrediente.unidad + "\n"

        string_dura_dificult = "\nDuracion: "+str(self.duracion)+" mins\n"+" Dificultad: "+self.dificultad
        string_elaboracion = "\nElaboracion \n" + self.elaboracion
        carta_receta = (self.nombre + "\n\n" + string_ingredientes + string_dura_dificult + string_elaboracion)

        print(carta_receta)
