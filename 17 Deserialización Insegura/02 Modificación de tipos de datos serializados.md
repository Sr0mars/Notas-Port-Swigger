En este laboratorio, la aplicación utiliza objetos PHP serializados dentro de una cookie de sesión. Al iniciar sesión como usuario legítimo, se puede interceptar y analizar la estructura del objeto.

La vulnerabilidad se explota modificando el tipo de dato del campo ‘**access_token**‘, convirtiéndolo de una cadena a un entero (**i:0**), y cambiando el nombre de usuario a ‘**administrator**‘, ajustando también la longitud del valor serializado.

Gracias a este cambio, la aplicación interpreta la sesión como si perteneciera al administrador. Esto permite acceder al panel de administración y eliminar al usuario carlos, resolviendo así el laboratorio.

Este ejemplo pone en evidencia cómo errores al verificar tipos de datos en objetos serializados pueden llevar a una suplantación completa de identidad.

Solucion
de igual manera nos logeamos y lo interceptamos y lo mandamos al repeater
![Pasted image 20250826205031.png](imagenes/Pasted image 20250826205031.png)
vamos a modificar la cookie en base64 quitando el usuario wiener y poniendo administrator y la cantidad de caracteres que tiene, de igual manera como no tenemos el access token del administrador vamos a quitarlo y poner un boleano que sea verdadero
tal que quedaria asi aplicamos los cambios
![Pasted image 20250826205309.png](imagenes/Pasted image 20250826205309.png)
le damos a send pero tenemos un error
![Pasted image 20250826205514.png](imagenes/Pasted image 20250826205514.png)
al parecer fueron por (:)
lo modificamos y le damos a send
![Pasted image 20250826205559.png](imagenes/Pasted image 20250826205559.png)
follow redirect
![Pasted image 20250826205623.png](imagenes/Pasted image 20250826205623.png)
pero vamos a regresarnos una anterior
![Pasted image 20250826205718.png](imagenes/Pasted image 20250826205718.png)
vamos a quitarle wiener y le damos send tal que ahora si tenemos administrador
![Pasted image 20250826205818.png](imagenes/Pasted image 20250826205818.png)
ahora nos vamos a admin y borramos al usuario
![Pasted image 20250826205951.png](imagenes/Pasted image 20250826205951.png)
![Pasted image 20250826210029.png](imagenes/Pasted image 20250826210029.png)


