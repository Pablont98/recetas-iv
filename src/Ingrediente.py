class Ingrediente:
    '''Clase que alberga los datos necesarios para guardar un ingrediente correctamente.'''

    def __init__(self, nombre, descripcion, vitaminas, precio, kcals_base, unidad, cantidad):
        self.nombre = nombre
        self.descripcion = descripcion
        self.vitaminas = vitaminas
        self.precio = precio
        self.kcals_base = kcals_base
        self.unidad = unidad
        self.cantidad = cantidad

    def kcals_totales(self):
        '''Método que calculará las kcals que tiene un ingrediente en base a su peso y a sus kcals base.'''
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
        return kcals_ingrediente_max