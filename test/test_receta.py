# Archivo para realizar tests a la clase Receta de nuestro proyecto

import pytest
import os
from src.Receta import *
from src.Ingrediente import *


@pytest.fixture
def receta():
    ingrediente_uno = Ingrediente('Patata', '', 'B,C', 0.90, 80, 'gramos', 1000)
    ingrediente_dos = Ingrediente('Cebolla', '', 'A,B6,C,E', 1, 40, 'gramos', 250)
    ingrediente_tres = Ingrediente('Pimiento', '', 'E,C', 0.90, 20, 'gramos', 500)
    ingrediente_cuatro = Ingrediente('Sal', '', '', 0.50, 0, 'gramos', 50)
    ingrediente_cinco = Ingrediente('Aceite', '', 'A,D,E,K',0.50, 2, 'mililitros', 350)
    lista_ingredientes = list()
    lista_ingredientes.append(ingrediente_uno)
    lista_ingredientes.append(ingrediente_dos)
    lista_ingredientes.append(ingrediente_tres)
    lista_ingredientes.append(ingrediente_cuatro)
    lista_ingredientes.append(ingrediente_cinco)
    elaboracion = "Cortar las patatas, las cebollas y los pimientos, lavar en agua, echar sal, echar el aceite " \
                   "en una sarten calentar y cuando el aceite este caliente freir las patatas, las cebollas y el pimiento"
    receta = Receta('Salteado de patatas', lista_ingredientes, 45, 'media',elaboracion)

    return receta

def test_kcals_ingrediente_max(receta):
    assert receta.ingredientes[0].kcals_totales() == 800

def test_kcals_max_receta(receta):
    assert receta.kcals_maximas() == 1294.65

def test_proteinas_max_receta(receta):
    assert receta.proteinas_maximas() == 27.75

def test_hidratos_max_receta(receta):
    assert receta.hidratos_maximos() == 182.25

def test_grasas_max_receta(receta):
    assert receta.grasas_maximas() == 356.8

