class Receta:
    '''Clase que alberga los datos necesarios para guardar una receta correctamente.'''

    def __init__(self, nombre, ingredientes, cantidades, duracion, dificultad, elaboracion):
        self.nombre = nombre
        self.ingredientes = list(ingredientes)
        self.cantidades = list(cantidades)
        self.duracion = duracion
        self.dificultad = dificultad
        self.elaboracion = elaboracion
        self.carta_receta = ''

    def kcals_maximas(self):
        ''' Método que calcula el aporte calórico total de la receta a partir de sus ingredientes.
            En este momento no se tendrá en cuenta la elaboración de la receta, ya que esta
            puede influir en el numero de calorias.'''
        kcals_max = 0
        contador = 0
        for ing in self.ingredientes:
            kcals_max += ing.kcals_totales(self.cantidades[contador])
            contador += 1
        return round(kcals_max,2)

    def hidratos_maximos(self):
        ''' Método que calcula el número de hidratos de la receta a partir de sus ingredientes.'''
        hidratos_max = 0
        contador = 0
        for ing in self.ingredientes:
            hidratos_max += ing.hidratos_totales(self.cantidades[contador])
            contador += 1
        return round(hidratos_max,2)

    def proteinas_maximas(self):
        ''' Método que calcula el número de proteinas de la receta a partir de sus ingredientes.'''
        proteinas_max = 0
        contador = 0
        for ing in self.ingredientes:
            proteinas_max += ing.proteinas_totales(self.cantidades[contador])
            contador += 1
        return round(proteinas_max,2)

    def grasas_maximas(self):
        ''' Método que calcula las grasas totales de la receta a partir de sus ingredientes.
            En este momento no se tendrá en cuenta la elaboración de la receta, ya que esta
            puede influir en el numero de grasas.'''
        grasas_max = 0
        contador = 0
        for ing in self.ingredientes:
            grasas_max += ing.grasas_totales(self.cantidades[contador])
            contador += 1
        return round(grasas_max,2)

    def visualizar_receta(self):
        '''Método que muestra una carta mostrando informacion referente a la receta'''
        string_ingredientes = ""
        contador = 0
        for ingrediente in self.ingredientes:
            string_ingredientes += ingrediente.nombre + " cantidad: " + str(self.cantidades[contador]) + " gramos\n"
            contador += 1

        string_dura_dificult = "\nDuracion: "+str(self.duracion)+" mins\n"+" Dificultad: "+self.dificultad
        string_elaboracion = "\nElaboracion \n" + self.elaboracion
        self.carta_receta = (self.nombre + "\n\n" + string_ingredientes + string_dura_dificult + string_elaboracion)

        print(self.carta_receta)
