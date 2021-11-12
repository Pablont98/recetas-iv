## Decisiones sobre el código

Se ha decidido organizar el código del proyecto de la siguiente manera:
* Tenemos la clase Ingrediente, la cual tendrá los siguientes atributos: 
  1. nombre y descripcion: ambas son cadenas de texto 
  3. vitaminas: lista que contiene las iniciales de las vitaminas (se le pasa una cadena texto pero en el init se extraen las iniciales de las vitaminas para incluirlas en la lista)
  4. precio: es un valor double
  5. kcals, proteinas, hidratos, grasas: valor double que significa la cantidad de dichos elementos por cada 100 gramos.
  Ademas de lo anterior se ha decidido que se implementen las funcionalidades del cálculo calorias, proteinas, hidratos y grasas de dichos ingredientes
  pasando como parámetro la cantidad de dicho ingrediente en la receta. 
  Se ha decidido que "cantidad" no sea un atributo de la clase para evitar hacer (por ejemplo) varios objetos ingrediente "patata" que lo unico que cambien sea
  la cantidad de dicho ingrediente. Se deja este atributo para la clase Receta y se pasa como parámetro en los métodos.
* Tenemos la clase Receta, la cual está explicada con detalle [aquí](https://github.com/Pablont98/IV/blob/Objetivo-4/docs/InformacionReceta.md).
  Como cambios a destacar Se añade el atributo cantidad que es una lista que contendrá las cantidades de cada ingrediente.
* La decisión de dejar las funcionalidades del cálculo de calorias, proteinas, hidratos y grasas de cada ingrediente dentro de la clase Ingrediente, es con la 
  idea de modularizar el código. Dejando los "temas/funciones" referentes al ingrediente dentro de este. Simplemente se le pasa como parámetro a esas funciones
  la cantidad y el se encarga de hacer el cálculo.
* Destacar que aun no se tiene en cuenta la elaboración para el cálculo de calorias y grasas (esta puede influir en el numero de calorias y grasas). Esto se
  resolverá mas adelante conforme el proyecto avance.
* Destacar que de momento se considera como unidad de medida de todos los elementos el gramo. Esto se resolverá/cambiará mas adelante conforme avance el proyecto.
