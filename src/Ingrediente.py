class Ingrediente:
    '''Clase que alberga los datos necesarios para guardar un ingrediente correctamente.'''

    def __init__(self, nombre, descripcion, vitaminas, precio, kcals_base, proteinas, hidratos, grasas, unidad, cantidad):
        self.nombre = nombre
        self.descripcion = descripcion
        self.vitaminas = vitaminas
        self.precio = precio
        self.kcals_base = kcals_base
        self.proteinas = proteinas
        self.hidratos = hidratos
        self.grasas = grasas
        self.unidad = unidad
        self.cantidad = cantidad

    def kcals_totales(self):
        '''Método que calculará las kcals que tiene un ingrediente en base a su cantidad y a sus kcals base.'''
        division = 1
        if(self.unidad == "gramos"):
            division = 100
        if(self.unidad == "mililitros"):
            division = 100
        if(self.unidad == "kilos"):
            division = 1
        if(self.unidad == "litros"):
            division = 1
        kcals_ingrediente_max = (self.kcals_base * self.cantidad) / division
        return round(kcals_ingrediente_max,2)

    def proteinas_totales(self):
        '''Metodo que calculara el numero de proteinas totales del ingrediente en base a la cantidad de dicho
           ingrediente Las proteinas se daran siempre en base a 100 gramos '''
        return round((self.proteinas * self.cantidad)/100,2)
        
    def hidratos_totales(self):
        '''Metodo que calculara el numero de hidratos totales del ingrediente en base a la cantidad de dicho
           ingrediente Los hidratos se daran siempre en base a 100 gramos '''
        return round((self.hidratos * self.cantidad)/100,2)

