## Necesidad de Integración continua

Con el objetivo de evitar una catástrofe al final de una larga fase de desarrollo, muchos equipos deciden aplicar integración continua 
con la que los cambios se implementan directamente en el proyecto. la integración continua es una práctica muy común sobre todo en el 
ámbito del desarrollo de software ágil. El objetivo de este moderno enfoque es trabajar a pasos pequeños con el fin de lograr un proceso 
de desarrollo más efectivo y poder reaccionar antes con más flexibilidad en los cambios.
Es por esto que se nos propone que eligamos dos sistemas de integración continua para: realizar test del proyecto con cada cambio en este y 
para probar las versiones del lenguaje válidas para nuestro proyecto.

## Elección y justificación de Sistemas de Integración continua

Al principio buscando información sobre distintos Sistemas de Integración continua ( [mirar aquí]( https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/herramientas-de-integracion-continua/) )
Mi idea era utilizar Circle CI y Semaphore CI (que aunque no venga en el enlace anterior, sabía con anterioridad de su existencia). 
También mire sistemas como Jenkins, GitLab CI o Travis CI, el problema de las dos primeras es que tenía que instalar la aplicación en mi pc y eso no me interesaba,
prefería un sistema el cual pudiera acceder por web (para mas comodidad) y por otro lado Travis CI es de pago y la versión gratuita requiere de introducir la 
tarjeta de crédito y eso no me llamaba para nada la atención.
El problema de Semaphore CI es que nunca me permitio utilizarlo, ya que a la hora de iniciar sesión me daba el siguiente error: 

```Oops, you can’t create a new Semaphore account because our abuse prevention system has detected a potential risk in your Github account. ```

Busque información sobre dicho problema por la red y por la página de ayuda de Semaphore CI pero no logré solucionar el problema, por lo que desistí de esta opción
y para no retrasarme mucho decidí utilizar Github Actions, dado que ya lo conozco de haberla utilizado en el objetivo anterior.
Con respecto a Circle CI su elección se llevo a cabo porque: 
* funciona con GitHub. 
* En las fases de prueba, pueden emplearse en contenedores o máquinas virtuales. 
* También arroja de forma automática builds compatibles con otros entornos.
* Su configuración se lleva a cabo con un archivo YAML.
* Soporta también el despliegue continuo. 
* Tiene alojamiento propio o en la nube. 
* Se ejecuta en contenedores Docker, máquinas virtuales Linux.
* Gratuita para un contenedor

Por todo lo expuesto anteriormente se decide: 
* Utilizar Circle CI para la ejecución de test con cada cambio en el proyecto.
* Github Actions para la prueba de versiones del lenguaje.
