class Ingrediente:
    '''Clase que alberga los datos necesarios para guardar un ingrediente correctamente.'''

    def __init__(self, nombre=None, descripcion=None, vitaminas=None, precio=None, kcals=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.vitaminas = vitaminas
        self.precio = precio
        self.kcals = kcals
