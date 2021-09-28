# Documentación correspondiente al objetivo-1 #

La aplicación esta pensada para ser usada principalmente por dos tipos de usuario:

1. Usuario alérgico: El cual busca un plan de comidas semanal, sin ánimo de crear dietas, que puedan suplir las carencias impuestas por su alergia.
		   Por ejemplo: si soy alérgico al huevo, enseñame comidas las cuales pueda comer sin problema o variantes (tortilla de patatas sin huevos).

2. Usuario "fit": El cual busca que la aplicación le genere una dieta (orientativa) de 7 días, siguiendo una serie 
	       de restricciones impuestas por el mismo usuario.
	       Si no se puede desarrollar una dieta con las restricciones impuestas se mostrara la dieta mas cercana 
	       a las restricciones impuestas por el usuario.
	       
3. Usuario estudiante: El cual busca ideas para hacer la comida con lo que tiene a mano. El usuario dice los ingredientes que tiene por casa y la aplicación
		       le muestra una posible receta con la que salir del paso.
	       
* De manera invisible al usuario que utilice dicha aplicación se hará un seguimiento de lo buscado/marcado por el usuario
para hacer un análisis sobre las preferencias de comidas de los usuarios. 

Ejemplo de lo anterior: 
> Usuarios registrados en un intervalo de edad de 18 a 24 años buscan frecuentemente comidas con el tag "pasta" y "comida rápida"
> Usuarios registrados en un intervalo de edad de 50 a 65 años buscan frecuentemente comidas con el tag "bajas en calorías"

## Descripción/perfil de usuarios: ##

1. Usuario alérgico (Paqui): Persona de entre 30-60 años, ama de casa, nivel de experiencia con apps: media-baja, es alérgica al huevo por lo que su margen de comidas es bastante limitado. Quiere que la aplicación le aporte un plan semanal de comidas variadas y alternativas a platos que tienen como ingrediente el huevo.

2. Usuario fit (Manuel): Persona de entre 20-30 años, deportista, nivel de experiencia con apps: alto, quiere una dieta orientativa que se ajuste a un numero determinado de calorías, gustos y intolerancias. Si no se puede determinar una dieta que se ajuste a sus peticiones, se le mostrara la dieta mas similar posible en cuanto a sus restricciones.

3. Usuario estudiante (Alba): Persona de entre 18-25 años, estudiante universitario, nivel de experiencia con apps: alto, tiene que comer antes de irse a la facultad pero tiene 4 ingredientes sueltos por casa y no le da tiempo de pasar por un supermercado ... Introduce en la aplicación los ingredientes que tiene y esta le facilita una receta con la que poder "salir del paso". 

## Descripción de dieta ##
Una dieta es una composición de recetas que siguen una serie de características impuestas por el usuario que la solicita. El usuario especificará el numero máximo de calorías que quiere que tenga dicha dieta e intolerancias alimentarias que pueda tener. La dieta se creará filtrando las características aportadas por el usuario con las recetas existentes en la aplicación.  
