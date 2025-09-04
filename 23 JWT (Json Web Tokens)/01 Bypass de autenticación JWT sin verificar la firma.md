En esta clase analizamos un fallo crítico en la implementación de tokens JWT: el servidor acepta cualquier token sin verificar su firma. Esto significa que podemos modificar el contenido del token sin necesidad de conocer la clave secreta.

Tras iniciar sesión con un usuario normal, interceptamos el JWT y cambiamos el valor del campo **sub** a **administrator**, accediendo así al panel de administración sin autenticación real. Desde allí, ejecutamos la acción de eliminar al usuario Carlos. Esta técnica demuestra la importancia de validar siempre la firma de un JWT para garantizar la integridad y autenticidad del token.

Solucion
![Pasted image 20250830214105.png](imagenes/Pasted image 20250830214105.png)
![Pasted image 20250830230017.png](imagenes/Pasted image 20250830230017.png)
La web:
![Pasted image 20250830225634.png](imagenes/Pasted image 20250830225634.png)
nos logeamos y vamos a interceptar esto
![Pasted image 20250830230036.png](imagenes/Pasted image 20250830230036.png)
miramos la cookie
![Pasted image 20250830230057.png](imagenes/Pasted image 20250830230057.png)
vamos a cambiarlo
![Pasted image 20250830230122.png](imagenes/Pasted image 20250830230122.png)
ahora si nos copiamos todo la cookie y si esta mal programado se supone que se debe validar
![Pasted image 20250830230357.png](imagenes/Pasted image 20250830230357.png)
y lo pegamos
![Pasted image 20250830230446.png](imagenes/Pasted image 20250830230446.png)
vemos el admin panel
![Pasted image 20250830230519.png](imagenes/Pasted image 20250830230519.png)
y ya solo eliminamos el usuario carlos
![Pasted image 20250830230603.png](imagenes/Pasted image 20250830230603.png)
