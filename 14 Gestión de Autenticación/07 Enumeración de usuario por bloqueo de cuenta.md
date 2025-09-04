En este laboratorio explotarás un fallo lógico en el sistema de bloqueo de cuentas para llevar a cabo una enumeración de usuarios. La aplicación bloquea temporalmente una cuenta tras varios intentos fallidos, pero la diferencia en los mensajes de error permite identificar qué nombres de usuario son válidos.

Usarás un ataque tipo cluster bomb en Burp Intruder para enviar varias solicitudes por cada nombre de usuario, provocando que las cuentas válidas sean bloqueadas y devuelvan un mensaje de error distinto. Una vez identificado el usuario, realizarás un ataque de fuerza bruta contra su contraseña utilizando un ataque tipo sniper. Tras esperar a que se levante el bloqueo temporal, iniciarás sesión con las credenciales obtenidas para resolver el laboratorio.

Solucion
vamos a interceptar un peticion de login en BS
asi que vamos a hacer un ataque de cluster bomb
![Pasted image 20250819222006.png](imagenes/Pasted image 20250819222006.png)
cargamos los payload y en settings hacemos la configuracion del grep extract
![Pasted image 20250819222157.png](imagenes/Pasted image 20250819222157.png)
