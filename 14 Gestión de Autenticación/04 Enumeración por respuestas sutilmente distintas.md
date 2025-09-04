En este laboratorio veremos cómo identificar un nombre de usuario válido mediante pequeñas diferencias en los mensajes de error que devuelve el servidor, y posteriormente realizar un ataque de fuerza bruta sobre su contraseña para acceder a su cuenta.

Todo el proceso se realiza desde Burp Intruder, apoyándonos en la función Grep – Extract para detectar variaciones mínimas en la respuesta que nos permitan distinguir usuarios existentes.

Una vez obtenido el usuario, atacaremos el campo de contraseña hasta obtener una combinación válida que nos permita iniciar sesión y acceder a su panel.

Solucion
de igual forma que en los otros laboratorios nos van a entregar un listado de usuario y contraseñas
![Pasted_image_20250819193139.png](/Imagenes/Pasted_image_20250819193139.png)
y bueno ya dentro del laboratiorio nos logeamos pero nos sale este error
![Pasted_image_20250819193336.png](/Imagenes/Pasted_image_20250819193336.png)
el cual ahora no nos dice si esta mal el usuario y la contraseaña si no que los 2 campos asi que lo que podemos hacer es un ataque de fuerza bruta
![Pasted_image_20250819193457.png](/Imagenes/Pasted_image_20250819193457.png)
asi que en este caso lo que podemos realizar es el mismo ataque pero en este punto vamos a configurar el grep que se encuentra ubicado en la parte de la derecha hasta el final
nos vamos a la parte del grep extract y le damos en refetch response
aqui seleccionamos en la parte del error que nos salia en el principio que es como un tipo warning
le damos ok
y le damos start attack
![Pasted_image_20250819193753.png](/Imagenes/Pasted_image_20250819193753.png)
en los resultado si filtramos en la parte del warning podemos ver que falta un punto
![Pasted_image_20250819194426.png](/Imagenes/Pasted_image_20250819194426.png)
y ahora aplicamos lo mismo con la contraseña
![Pasted_image_20250819195231.png](/Imagenes/Pasted_image_20250819195231.png)
![Pasted_image_20250819195316.png](/Imagenes/Pasted_image_20250819195316.png)
