# Informacion sobre la clase Receta

la clase Receta es la clase que se va a testear en el objetivo-4 de la asignatura IV. Dicha clase recoge como su nombre indica toda la información
necesaria para llevar a cabo una determinada receta.

Los atributos de los que se compone pasan por:

* Nombre de la receta (cadena de texto)
* Ingredientes (Esto es una lista de objetos de la clase Ingrediente)
* Cantidades (Lista de double con la cantidad de cada Ingrediente, de momento la unidad de medida referente a estas cantidades son los gramos)
* Duración de la receta (entero con unidad minutos)
* Dificultad de la receta (entero entre 1 y 5)
* Explicación de la receta (cadena de texto)

Sus metodos hasta ahora implementados:

* kcals_maximas (cálculo de calorias máximas de la receta)
* hidratos_maximos (cálculo de hidratos máxmios de la receta)
* proteinas_maximas (cálculo de proteinas máximas de la receta)
* grasas_maximas (cálculo de grasas máximas de la receta)
* visualizar_receta (metodo que nos muestra por pantalla una carta de receta)

Para ver el correcto funcionamiento de esta clase, se llevará acabo un test que sea capaz de crear una objeto Receta y realizar un calculo del total de calorias, 
proteinas, hidratos y grasas que contiene dicha receta. 

> No se ha tenido en cuenta la elaboración de la receta para el cálculo de calorias y grasas de esta, ya que la elaboración puede influir en estos valores.
> Esta problemática se resolverá mas adelante, conforme el proyecto avance.
