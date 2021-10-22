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

* Objetivo 1 - [Documentación correspondiente al objetivo-1](docs/HU.md)

* Objetivo 3 - [Justificación de elección de task runner para el proyecto](docs/obj3.md)

* Objetivo 4 - [Clase Receta que se va a testear](docs/InformacionReceta.md)

## Instalación y uso

Descargar los archivos fuente de este repositorio de manera directa desde github o [clonándolo](https://docs.github.com/es/repositories/creating-and-managing-repositories/cloning-a-repository)
Con el proyecto ya descargado:
1. Abrimos una terminal en el directorio raíz del proyecto.
2. [Instalamos Invoke](https://www.pyinvoke.org/installing.html) con el siguiente comando: ```pip install invoke```
3. Ahora instalamos las dependencias con el siguiente comando: ```invoke installdeps```
4. Para correr los test y comprobar que todo funciona bien, escribimos el siguiente comando: ```invoke test```

* Para comprobar que la sintaxis de los ficheros del módulo que se está ejecutando es la correcta podemos escribir el siguiente comando: ```invoke check```
