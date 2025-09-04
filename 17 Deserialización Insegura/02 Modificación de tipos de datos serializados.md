En este laboratorio, la aplicación utiliza objetos PHP serializados dentro de una cookie de sesión. Al iniciar sesión como usuario legítimo, se puede interceptar y analizar la estructura del objeto.

La vulnerabilidad se explota modificando el tipo de dato del campo ‘**access_token**‘, convirtiéndolo de una cadena a un entero (**i:0**), y cambiando el nombre de usuario a ‘**administrator**‘, ajustando también la longitud del valor serializado.

Gracias a este cambio, la aplicación interpreta la sesión como si perteneciera al administrador. Esto permite acceder al panel de administración y eliminar al usuario carlos, resolviendo así el laboratorio.

Este ejemplo pone en evidencia cómo errores al verificar tipos de datos en objetos serializados pueden llevar a una suplantación completa de identidad.

Solucion
de igual manera nos logeamos y lo interceptamos y lo mandamos al repeater
![Pasted_image_20250826205031.png](/Imagenes/Pasted_image_20250826205031.png)
vamos a modificar la cookie en base64 quitando el usuario wiener y poniendo administrator y la cantidad de caracteres que tiene, de igual manera como no tenemos el access token del administrador vamos a quitarlo y poner un boleano que sea verdadero
tal que quedaria asi aplicamos los cambios
![Pasted_image_20250826205309.png](/Imagenes/Pasted_image_20250826205309.png)
le damos a send pero tenemos un error
![Pasted_image_20250826205514.png](/Imagenes/Pasted_image_20250826205514.png)
al parecer fueron por (:)
lo modificamos y le damos a send
![Pasted_image_20250826205559.png](/Imagenes/Pasted_image_20250826205559.png)
follow redirect
![Pasted_image_20250826205623.png](/Imagenes/Pasted_image_20250826205623.png)
pero vamos a regresarnos una anterior
![Pasted_image_20250826205718.png](/Imagenes/Pasted_image_20250826205718.png)
vamos a quitarle wiener y le damos send tal que ahora si tenemos administrador
![Pasted_image_20250826205818.png](/Imagenes/Pasted_image_20250826205818.png)
ahora nos vamos a admin y borramos al usuario
![Pasted_image_20250826205951.png](/Imagenes/Pasted_image_20250826205951.png)
![Pasted_image_20250826210029.png](/Imagenes/Pasted_image_20250826210029.png)


