En esta clase exploramos un XSS almacenado que se produce dentro de un atributo de tipo enlace. La funcionalidad vulnerable es el sistema de comentarios del blog, que permite introducir un nombre, correo y un sitio web. El valor del sitio web se utiliza como destino en un enlace generado automáticamente alrededor del nombre del autor del comentario.

El sistema codifica las comillas dobles, pero no valida ni restringe el contenido del enlace. Esto permite introducir un esquema especial como dirección, el cual no apunta a una página web sino que ejecuta directamente código cuando el usuario hace clic.

Aprovechamos este comportamiento para insertar un valor que desencadena una acción maliciosa cuando alguien interactúa con el nombre del autor. Al tratarse de un XSS almacenado, el código queda persistente en la aplicación y se ejecutará para cualquier visitante que visualice ese comentario.

Este laboratorio muestra cómo vectores aparentemente inofensivos, como un campo de URL opcional, pueden utilizarse para comprometer la seguridad de otros usuarios si no se implementan controles adecuados.

Solucion
Aprovechandonos del la parte de comentarios podemos poner esto abusando del href javascript:alert(0)
![Pasted image 20250707161132.png](imagenes/Pasted image 20250707161132.png)
Cuando nosotros le damos click al nombre nos redirige a otro hipervinculo
![Pasted image 20250707161221.png](imagenes/Pasted image 20250707161221.png)


