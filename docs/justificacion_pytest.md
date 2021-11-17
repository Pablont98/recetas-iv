### Justificación de elección de pytest

Necesitabamos testear el funcionamiento actual y el estado de nuestro proyecto, por lo que se investigó que herramienta de tests sería la adecuada. 
Al final se optó por la utilización de pytest para testear la aplicación debido a la comodidad que suponía por tener una sintaxis simple, por incluir fixtures 
y por su biblioteca assert la cual nos va a ser bastante util y simple de utilizar también.

* Fixtures: Objetos que si no se crean de forma correcta, indican que algo esta mal. Si estos objetos se crean correctamente, 
            se usaran como base para las posteriores funciones de test.

* Assert: Comprueba que la expresión pasada como argumento en el test sea correcta. Simplemente metemos lo que queramos comprobar en los corchetes de assert()
          y este nos indicará si la comprobación es correcta o no, además nos lanzará errores si hay fallos en nuestro código.

Ademas de todo lo anterior, también influyó en su elección que en caso de algún fallo o problema hay una extensa documentación e información y un gran numero de foros a los que acudir.
