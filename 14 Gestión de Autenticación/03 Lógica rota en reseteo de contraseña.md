En esta clase explotamos un fallo lógico crítico en el sistema de recuperación de contraseñas.

El servidor permite cambiar la contraseña sin validar el token enviado por email, lo que nos permite interceptar nuestra propia solicitud de cambio, eliminar el token y modificar el nombre de usuario por el de Carlos. De este modo, reasignamos su contraseña y tomamos control total de su cuenta.

Solucion
en este caso nos han proporcio nado un usuario pero aqui lo que vmaos hacer es picarle en el boton de no recuerdo mi contraseña de modo que este actuara de manera inmediata mandandonos un correo
![Pasted_image_20250819191338.png](Imagenes/Pasted_image_20250819191338.png)
entonces nosotro necesitamos indicarle que usuario es
![Pasted_image_20250819191504.png](Imagenes/Pasted_image_20250819191504.png)
aqui nos llega el correo asi que vamos a interceptar ese link
![Pasted_image_20250819191535.png](Imagenes/Pasted_image_20250819191535.png)
![Pasted_image_20250819191714.png](Imagenes/Pasted_image_20250819191714.png)
de igual manera vamos a interceptar el cambio de contraseña poniendo (test)
![Pasted_image_20250819191840.png](Imagenes/Pasted_image_20250819191840.png)
aqui que podemos hacer lo primero seria eliminar los 2 token que se ven arriba y cambiar en la parte de abajo el usuario wiener por el de carlos
![Pasted_image_20250819192209.png](Imagenes/Pasted_image_20250819192209.png)
le damos a send y despues follow redirection
![Pasted_image_20250819192243.png](Imagenes/Pasted_image_20250819192243.png)
![Pasted_image_20250819192306.png](Imagenes/Pasted_image_20250819192306.png)
y probamos ahora la nueva contraseña que seria test
![Pasted_image_20250819192408.png](Imagenes/Pasted_image_20250819192408.png)
