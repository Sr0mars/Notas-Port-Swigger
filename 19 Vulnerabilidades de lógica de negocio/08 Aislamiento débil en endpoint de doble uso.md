En esta clase vemos cómo un endpoint diseñado para el cambio de contraseña puede ser reutilizado de forma maliciosa por falta de aislamiento lógico. Aunque normalmente se solicita la contraseña actual para realizar el cambio, al eliminar este parámetro en la petición y modificar el valor del campo username a administrator, logramos modificar directamente la contraseña del administrador.

Esto ocurre porque el sistema no valida adecuadamente que la solicitud provenga del usuario autenticado. Tras cambiar la contraseña, accedemos como administrador y eliminamos al usuario carlos, completando así el laboratorio.

Solucion
nos logeamos primero pero despues de que nos logeamos podemos ver que podemos cambiar nuestra contraseña por lo cual esto lo vamos a interceptar y lo vamos a mandar al repeater
![Pasted image 20250828224837.png](imagenes/Pasted image 20250828224837.png)
por lo cual si nosotros ponemos otro usuario
![Pasted image 20250828225112.png](imagenes/Pasted image 20250828225112.png)
pero que pasa si quitamos el current password
![Pasted image 20250828225254.png](imagenes/Pasted image 20250828225254.png)
nos sale que es correcta la contraseña
y que pasa si ahora cambiamos el usuario a administrator
![Pasted image 20250828225433.png](imagenes/Pasted image 20250828225433.png)
lo probamos
![Pasted image 20250828225523.png](imagenes/Pasted image 20250828225523.png)
![Pasted image 20250828225603.png](imagenes/Pasted image 20250828225603.png)
ya solo entramos al admin panel y eliminamos al usuario
![Pasted image 20250828225631.png](imagenes/Pasted image 20250828225631.png)
