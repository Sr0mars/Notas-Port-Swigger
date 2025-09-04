Este laboratorio demuestra cómo un atacante puede combinar una vulnerabilidad de XSS almacenado con el uso indebido de cookies para llevar a cabo un ataque de cracking offline.

La aplicación utiliza una cookie persistente que contiene el nombre de usuario y un hash MD5 de su contraseña, codificados en Base64. Al analizar la cookie generada al iniciar sesión con una cuenta propia, se descubre su estructura: usuario:md5(contraseña).

El siguiente paso es aprovechar un XSS almacenado en los comentarios del blog para robar la cookie del usuario víctima, Carlos. Usando un payload JavaScript, el atacante redirige la cookie del navegador de Carlos hacia su servidor de explotación.

Una vez recibida la cookie, se decodifica y se extrae el hash MD5. Con ese hash, es posible hacer un ataque offline (o incluso una simple búsqueda en Google si la contraseña es débil) para descubrir la contraseña original.

Finalmente, conociendo las credenciales, el atacante inicia sesión como Carlos y elimina su cuenta desde la sección “My account”, resolviendo así el laboratorio.

Solucion
asi que por ahora lo que vamos a realizar es una busquedad por BS de la navegacion de la pagina
![Pasted_image_20250820214634.png](/Imagenes/Pasted_image_20250820214634.png)
probamos todo lo que hicimos en el laboratorio anterior pero no funciona pasamoa a explorar tenemos  un exploit server y tal parace que en la parte de comentarios la seccion es vulnerable a xss asi que vamos a injectar un payload
