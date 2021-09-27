# Documentación correspondiente al objetivo-1 #

La aplicación esta pensada para ser usada principalmente por dos tipos de usuario:

1. Usuario casual: El cual busca recetas de manera independiente, sin ánimo de crear dietas, ni nada por el estilo.
		   (Típico usuario que no sabe que hacer de comer y busca algo que le llame la atención)
		   Si no se encuentra una receta con los requisitos dados se le mostrara recetas lo mas parecidas a lo buscado

2. Usuario "fit": El cual busca que la aplicación le genere una dieta (orientativa) de 7 días, siguiendo una serie 
	       de restricciones impuestas por el mismo usuario.
	       Si no se puede desarrollar una dieta con las restricciones impuestas se mostrara la dieta mas cercana 
	       a las restricciones impuestas por el usuario
	       
* De manera invisible al usuario que utilice dicha aplicación se hará un seguimiento de lo buscado/marcado por el usuario
para hacer un análisis sobre las preferencias de comidas de los usuarios. 

Ejemplo de lo anterior: 
> Usuarios registrados en un intervalo de edad de 18 a 24 años buscan frecuentemente comidas con el tag "pasta" y "comida rápida"
> Usuarios registrados en un intervalo de edad de 50 a 65 años buscan frecuentemente comidas con el tag "bajas en calorías"

## Descripción/perfil de usuarios: ##

1. Usuario casual (Paqui): Persona de entre 30-60 años, ama de casa, nivel de experiencia con apps: media-baja, no sabe que hacer de comer hoy y busca una receta fácil y buena que se ajuste a sus gustos, intolerancias y a los de su familia. Si no existe una receta que se ajuste a lo que busque, se le mostraran recetas lo mas similares posibles.

2. Usuario fit (Manuel): Persona de entre 20-30 años, deportista, nivel de experiencia con apps: alto, quiere una dieta orientativa que se ajuste a un numero determinado de calorías, gustos y intolerancias. Si no se puede determinar una dieta que se ajuste a sus peticiones, se le mostrara la dieta mas similar posible en cuanto a sus restricciones.

## Descripcion de dieta ##
Una dieta es una composición de recetas que siguen una serie de características impuestas por el usuario que la solicita. El usuario especificará el numero máximo de calorias que quiere que tenga dicha dieta e intolerancias alimentarias que pueda tener. La dieta se creará filtrando las caracteristicas aportadas por el usuario con las recetas existentes en la aplicación.  
