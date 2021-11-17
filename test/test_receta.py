# Archivo para realizar tests a la clase Receta de nuestro proyecto

import pytest
from src.receta import *
from src.ingrediente import *


@pytest.fixture
def receta():
    ingrediente_uno = Ingrediente('Patata', '', 'B,C', 0.90, 80, 2.2, 16.1, 0.2)
    ingrediente_dos = Ingrediente('Cebolla', '', 'A,B6,C,E', 1, 32, 1.1, 5.3, 0.2)
    ingrediente_tres = Ingrediente('Pimiento verde', '', 'E,C', 0.90, 20, 0.6, 1.6, 0.8)
    ingrediente_cuatro = Ingrediente('Sal', '', '', 0.50, 0, 0, 0, 0)
    ingrediente_cinco = Ingrediente('Aceite de oliva', '', 'A,D,E,K',2.50, 899, 0, 0, 99.9)
    lista_ingredientes = list()
    lista_ingredientes.append(ingrediente_uno)
    lista_ingredientes.append(ingrediente_dos)
    lista_ingredientes.append(ingrediente_tres)
    lista_ingredientes.append(ingrediente_cuatro)
    lista_ingredientes.append(ingrediente_cinco)
    lista_cantidades = [1000,250,500,10,350]
    elaboracion = "Cortar las patatas, las cebollas y los pimientos, lavar en agua, echar sal, echar el aceite " \
                   "en una sarten calentar y cuando el aceite este caliente freir las patatas, las cebollas y el pimiento"
    receta = Receta('Salteado de patatas', lista_ingredientes, lista_cantidades, 45, 'media',elaboracion)

    return receta

def test_kcals_ingrediente_max(receta):
    assert receta.ingredientes[0].kcals_totales(receta.cantidades[0]) == 800

def test_kcals_max_receta(receta):
    assert receta.kcals_maximas() == 4126.5

def test_proteinas_max_receta(receta):
    assert receta.proteinas_maximas() == 27.75

def test_hidratos_max_receta(receta):
    assert receta.hidratos_maximos() == 182.25000000000003

def test_grasas_max_receta(receta):
    assert receta.grasas_maximas() == 356.15

