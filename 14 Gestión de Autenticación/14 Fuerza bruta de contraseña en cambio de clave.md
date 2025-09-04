En este laboratorio aprovechamos una lógica defectuosa en la funcionalidad de cambio de contraseña para realizar un ataque de fuerza bruta contra la contraseña actual de Carlos.

El endpoint de cambio de contraseña revela diferentes mensajes de error dependiendo del estado de validación de los datos enviados. En particular, si el password actual es incorrecto pero los nuevos no coinciden, muestra un mensaje genérico. Sin embargo, si el password actual es correcto pero los nuevos no coinciden, muestra específicamente que las nuevas contraseñas no coinciden. Esto nos permite detectar cuándo una contraseña actual es válida sin necesidad de cambiar realmente la contraseña.

Configuramos un ataque en Burp Intruder usando como objetivo el campo ‘**current-password**‘, y dejamos intencionalmente diferentes valores en los campos ‘**new-password-1**‘ y ‘**new-password-2**‘. Aplicamos una regla de búsqueda que identifique las respuestas con el texto New passwords do not match, lo que nos permitirá detectar cuándo la contraseña actual es válida.

Una vez identificada la contraseña correcta, simplemente iniciamos sesión como Carlos y accedemos a su panel para resolver el laboratorio.

Solucion
tenemos un apartado modificable
![Pasted image 20250820223542.png](imagenes/Pasted image 20250820223542.png)
asi que vamos  a interceptarlo poniendo contraseñas incorrectas
![Pasted image 20250820223959.png](imagenes/Pasted image 20250820223959.png)bueno vemos que tenemos diferentes campos podemos hacer que username cambie lo cual es malo
![Pasted image 20250820224101.png](imagenes/Pasted image 20250820224101.png)
asi que esto lo mandamos al intruder cual campo de current-password vamos a usarlo de payload, agregamos el diccionario y en grep extract ponemos el error que nos sale
![Pasted image 20250820224509.png](imagenes/Pasted image 20250820224509.png)
y empezamos el ataque
![Pasted image 20250820224801.png](imagenes/Pasted image 20250820224801.png)
parece ser que tenemos una nueva contraseña
ahora nos logeamos como carlos y un nuevo usuario
![Pasted image 20250820224919.png](imagenes/Pasted image 20250820224919.png)



