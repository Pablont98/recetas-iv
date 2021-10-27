class Ingrediente:
    '''Clase que alberga los datos necesarios para guardar un ingrediente correctamente.'''

    def __init__(self, nombre, descripcion, vitaminas, precio, kcals_base, unidad, cantidad):
        self.nombre = nombre
        self.descripcion = descripcion
        self.vitaminas = vitaminas
        self.precio = precio
        self.kcals_base = kcals_base
        self.unidad = unidad

    def kcals_totales():
        '''Método que calculará las kcals que tiene un ingrediente en base a su peso y a sus kcals base.'''
        pass
