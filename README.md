# IV-App de recetas
Repositorio creado para la asignatura de Infraestructura Virtual, curso 2021/22

El proyecto a abordar es una aplicación de PC dedicada a recetas de cocina 
a modo de libro de recetas digital.

En esta aplicación se podrán tanto consultar recetas de manera independiente según nuestros gustos,
como solicitar a la aplicación que nos diseñe una dieta orientativa de 7 días según nuestras restricciones
calóricas, intolerancias, etc.

Se ha abordado el proyecto de esta manera con la idea de darle mas variedad al usuario y no sea simplemente solo 
una pagina en la consultar recetas.

Se ira actualizando este archivo con los distintos cambios que vaya teniendo el proyecto

## Documentación adicional de objetivos

* Objetivo 1 - [Documentación correspondiente al objetivo-1](https://github.com/Pablont98/recetas-iv/blob/main/docs/HU.md)

* Objetivo 3 - [Justificación de elección de task runner para el proyecto](https://github.com/Pablont98/recetas-iv/blob/main/docs/obj3.md)

* Objetivo 4 - [Clase Receta que se va a testear](https://github.com/Pablont98/recetas-iv/blob/main/docs/InformacionReceta.md), [Justificación de uso de pytest](https://github.com/Pablont98/recetas-iv/blob/main/docs/justificacion_pytest.md) y [Decisiones de código tomadas](https://github.com/Pablont98/IV/blob/Objetivo-4/docs/decisiones_codigo.md)

* Objetivo 6 - [Documentación de elección y justificación de sistemas de Integración Continua](https://github.com/Pablont98/recetas-iv/blob/Objetivo-6/docs/IntegracionContinua.md)

## Instalación y uso

Descargar los archivos fuente de este repositorio de manera directa desde github o [clonándolo](https://docs.github.com/es/repositories/creating-and-managing-repositories/cloning-a-repository)
Con el proyecto ya descargado:
1. Abrimos una terminal en el directorio raíz del proyecto.
2. [Instalamos Invoke](https://www.pyinvoke.org/installing.html) con el siguiente comando: ```pip install invoke```
3. Ahora instalamos las dependencias con el siguiente comando: ```invoke installdeps```
4. Para correr los test y comprobar que todo funciona bien, escribimos el siguiente comando: ```invoke test```
* Para comprobar que la sintaxis de los ficheros del módulo que se está ejecutando es la correcta podemos escribir el siguiente comando: ```invoke check```

## Contenedor de pruebas
Para la creación del contenedor se ha creado un archivo [Dockerfile](https://github.com/Pablont98/recetas-iv/blob/Objetivo-5/Dockerfile) el cual realiza los 
pasos necesarios para la correcta creación de dicho contenedor. Como contenedor base se ha optado por el Python3.8-slim-buster, ya que, queremos que nuestro
contenedor de test corra con la versión 3.8 de Python y ademas la versión slim-buster hace que el contenedor base no sea muy pesado, lo cual es una
gran ventaja, ya que de 378MB que ocupa hacer el contendor con la version Python 3.8 oficial, con slim-buster se queda entorno a los 70/80MB. 
Dicho contenedor lo utilizaremos para ejecutar nuestros test. La instalación de dependencias, módulos, bibliotecas,
etc. Son transparentes al usuario.
> para realizar los tests dentro de este contenedor se tendrá que disponer de la herramienta docker en nuestro sistema.
* Se recomienda hacer pull de este repositorio en DockerHub con la siguiente linea en nuestra terminal: ```docker pull pablont98/recetas-iv```.
* Tras esto nos descargamos este repositorio desde github y nos posicionamos dentro de el.
* Por último escribimos lo siguiente en la terminal: ```docker run -t -v `pwd`:/app/test pablont98/recetas-iv```.

Enlace del repositorio en DockerHub [pablont98/recetas-iv](https://hub.docker.com/repository/docker/pablont98/recetas-iv/general)

## Integración continua - Prueba de versiones
Se ha decidido probar las versiones de la 3.6 a la 3.10 de Python, ya que, son todas las versiones que en 2021 son funcionales. 
Todas esas versiones funcionan correctamente en el proyecto ya que aun no utiliza bibliotecas las cuales no funcionen en versiones como la 3.6 o 3.7.
En el futuro, con el avance del proyecto y de su código, posiblemente (seguramente) hagan falta el uso de bibliotecas que no soporten versiones como la
3.6 o 3.7 en ese momento se redefinirá la matrix de la Github Action hasta la versión minima posible (la primera que no de error).
Por el momento la versión minima es la 3.6 y la máxima 3.10, que si bien aun no se considera una versión estable, podemos tener cierta certeza de que 
el código del proyecto escrito por el momento se ejecutará sin problema en esa versión.

## Información adicional
* Se ha elegido Poetry como gestor de dependencias, para así poder ajustarnos a las buenas prácticas de Python las cuales ya no hacen uso de requirements.txt sino
  de pyproject.toml. La instalación y uso de este será transparente al usuario ya que se instala desde la orden ```invoke installdeps```. 
* A la hora de realizar los test no se han tenido en cuenta aun situaciones como el metodo de elaboración de la receta para el cálculo de calorias y grasas. Ya 
  que la elaboración puede influir en la absorción o perdidas de estos componentes.
* De momento la unidad de medida de todos los ingredientes es el gramo. 
> Estos dos últimos puntos se iran resolviendo con el avance del proyecto.
