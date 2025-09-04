En este laboratorio, explotamos una vulnerabilidad de password reset poisoning manipulando el encabezado ‘**X-Forwarded-Host**‘. La aplicación genera enlaces de restablecimiento de contraseña utilizando este encabezado sin validarlo correctamente, lo que nos permite redirigir el enlace generado al dominio del servidor de explotación.

Solicitamos el restablecimiento de contraseña para el usuario Carlos, añadiendo nuestro propio ‘**X-Forwarded-Host**‘ apuntando al exploit server. Carlos, al hacer clic en el enlace manipulado, realiza una petición a nuestro servidor y nos filtra el token de reseteo en la URL.

Una vez obtenido ese token, lo usamos para construir una URL de reseteo válida, pero con el token robado, lo que nos permite cambiar la contraseña de Carlos sin que él lo sepa. Finalmente, accedemos a su cuenta utilizando la nueva contraseña y resolvemos el laboratorio.

Solucion
viendo un poco la web vemos que como anteriores labarotorios podemos ver que tenemos un apartado de olvido su contraseña y todo ese proceso lo vamos a interceptar
![Pasted_image_20250820221835.png](Imagenes/Pasted_image_20250820221835.png)
la peticion por post la mandamos al repeter
y en nuestro exploit server en el apartado de email podemos ver claramente que nos llega un link para cambiar la contraseña
![Pasted_image_20250820222125.png](Imagenes/Pasted_image_20250820222125.png)
asi que en este punto vamos a jugar con otra cabecera (**X-Forwarded-Host**) que nos permite por medio de la url cambiar la url
![Pasted_image_20250820222456.png](Imagenes/Pasted_image_20250820222456.png)
como nos llegaria al correo
![Pasted_image_20250820222522.png](Imagenes/Pasted_image_20250820222522.png)
entonces lo que podemos hacer es configurar en el BS estos parametros y se lo enviamos a carlos y de nuestra parte solo seria esperar y mirar los logs
![Pasted_image_20250820222832.png](Imagenes/Pasted_image_20250820222832.png)
le damos send
recargamos
![Pasted_image_20250820222906.png](Imagenes/Pasted_image_20250820222906.png)
y lo reemplazamos de una peticion vieja de correo
![Pasted_image_20250820223010.png](Imagenes/Pasted_image_20250820223010.png)
cambiamos la contraseña
![Pasted_image_20250820223043.png](Imagenes/Pasted_image_20250820223043.png)
y ya solo nos logeamos
![Pasted_image_20250820223129.png](Imagenes/Pasted_image_20250820223129.png)
