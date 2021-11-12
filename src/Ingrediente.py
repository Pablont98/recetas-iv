class Ingrediente:
    '''Clase que alberga los datos necesarios para guardar un ingrediente correctamente.'''

    def __init__(self, nombre, descripcion, vitaminas, precio, kcals, proteinas, hidratos, grasas):
        self.nombre = nombre
        self.descripcion = descripcion
        self.vitaminas = list()
        for caracter in vitaminas:
            if caracter != ',' or caracter != ' ':
                self.vitaminas = caracter

        self.precio = precio
        self.kcals = kcals
        self.proteinas = proteinas
        self.hidratos = hidratos
        self.grasas = grasas

    def kcals_totales(self, cantidad):
        '''Método que calculará las kcals que tiene un ingrediente en base a su cantidad y a sus kcals base.
           En este momento se considerará como unidad gramos a todos los ingredientes.'''
        kcals_ingrediente_max = (self.kcals * cantidad) / 100
        return round(kcals_ingrediente_max,2)

    def proteinas_totales(self, cantidad):
        '''Metodo que calculará el número de proteinas totales del ingrediente en base a la cantidad de dicho
           ingrediente Las proteinas se daran siempre en base a 100 gramos '''
        return round((self.proteinas * cantidad)/100,2)

    def hidratos_totales(self, cantidad):
        '''Metodo que calculará el número de hidratos totales del ingrediente en base a la cantidad de dicho
           ingrediente Los hidratos se daran siempre en base a 100 gramos '''
        return round((self.hidratos * cantidad)/100,2)

    def grasas_totales(self, cantidad):
        '''Metodo que calculará el número de grasas totales del ingrediente en base a la cantidad de dicho
           ingrediente. Las grasas se daran siempre en base a 100 gramos '''
        return round((self.grasas * cantidad)/100,2)
