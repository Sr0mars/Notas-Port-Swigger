En esta clase vemos cómo un sistema de 2FA mal implementado puede ser trivialmente eludido. Tras autenticarnos con las credenciales de Carlos, el sistema solicita el código de verificación.

Sin embargo, al modificar manualmente la URL hacia la sección de perfil, conseguimos saltarnos la segunda verificación y acceder a la cuenta. Un fallo grave derivado de no proteger rutas sensibles tras el login.

Solucion
en este laboratorio nos entregan credencial de un usuario pero cuando terminamos de logearnos nos pide que ingresemos un codigo
![Pasted image 20250819190400.png](imagenes/Pasted image 20250819190400.png)
si nosotro le damos al email client podemos ver que nos llego un correo
![Pasted image 20250819190439.png](imagenes/Pasted image 20250819190439.png)
y bueno podemos ver que nos entrega las credenciales correctas
![Pasted image 20250819190638.png](imagenes/Pasted image 20250819190638.png)
pero podemos ver que se aplica un redirect asi que lo que podemos hacer es logeranos con carlos y aplicar un redirect para ver si nos deja
![Pasted image 20250819190740.png](imagenes/Pasted image 20250819190740.png)
![Pasted image 20250819190820.png](imagenes/Pasted image 20250819190820.png)
y bueno no tiene ningun tipo de sanitizacion
![Pasted image 20250819190848.png](imagenes/Pasted image 20250819190848.png)
