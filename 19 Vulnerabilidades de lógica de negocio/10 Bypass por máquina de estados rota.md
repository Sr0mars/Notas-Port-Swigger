En esta clase explotamos un fallo en la lógica de la máquina de estados del proceso de autenticación. Tras hacer login, la aplicación nos redirige a una página para seleccionar el rol del usuario. Sin embargo, si interceptamos y descartamos la solicitud de selección de rol justo después de autenticarnos, y accedemos directamente al sitio, la aplicación asume por defecto el rol de administrador.

Esto nos permite acceder al panel de administración sin autorización legítima y eliminar al usuario Carlos para completar el laboratorio.

Solucion
nos logeamos y despues de logearnos no sale que podemos cambiar de rol lo vamos a interceptar
![[Pasted image 20250828231537.png]]nos sale esta intercepcion vamos a modificar user por administrator y lo mandamos al repeater y le damos send y follow redirect
![[Pasted image 20250828231656.png]]
![[Pasted image 20250828231805.png]]
y no  ah pasado nada
![[Pasted image 20250828231904.png]]
vamos a volver a intentarlo pero vamos a interceptar el login
![[Pasted image 20250828231954.png]]
le damos a forward y la siguiente solicitud vamos a dropearla
![[Pasted image 20250828232039.png]]
![[Pasted image 20250828232115.png]]
pero si ahora nos vamos a la raiz
se ve que aqui nos da el admin panel
![[Pasted image 20250828232154.png]]
y ya solo eliminamos al usuario
![[Pasted image 20250828232225.png]]