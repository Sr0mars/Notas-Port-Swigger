En esta clase trabajamos con un fallo común en formularios de autenticación: respuestas distintas para usuarios inválidos y contraseñas incorrectas. Aprovechamos esta diferencia para enumerar usuarios válidos mediante Burp Intruder.

Una vez identificado un usuario real, realizamos fuerza bruta sobre su contraseña hasta conseguir acceso. Un ejemplo claro de cómo la inconsistencia en los mensajes de error compromete la seguridad del login.

Solucion
La web:
![Pasted image 20250819183622.png](imagenes/Pasted image 20250819183622.png)
vamos a interceptar esto
![Pasted image 20250819183829.png](imagenes/Pasted image 20250819183829.png)
y lo vamos a mandar al intruder (Ctrl+i)
![Pasted image 20250819184026.png](imagenes/Pasted image 20250819184026.png)
asi que vamos a implementar un ataque de fuerza bruta con unos usuarios que nos dan
![Pasted image 20250819184334.png](imagenes/Pasted image 20250819184334.png)
tambien unas contraseñas
![Pasted image 20250819184612.png](imagenes/Pasted image 20250819184612.png)
asi que las almacenamos y cargamos en payload
![Pasted image 20250819184718.png](imagenes/Pasted image 20250819184718.png)
hacemos el ataque y podemos ver que el ataque se efectua por que en el length tenemo una cantidad diferente que otro por lo cual
el usuario (acid) es probable candidato
![Pasted image 20250819185327.png](imagenes/Pasted image 20250819185327.png)
y hacemos el otro ataque con las contraseñas
![Pasted image 20250819185935.png](imagenes/Pasted image 20250819185935.png)
y lo ponemos
![Pasted image 20250819190004.png](imagenes/Pasted image 20250819190004.png)
