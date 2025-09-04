En esta primera parte del laboratorio, examinamos la cookie de sesión y detectamos que contiene un objeto serializado en formato Ruby (Marshal). Al no disponer de acceso al código fuente, recurrimos a la búsqueda de exploits conocidos.

Localizamos un gadget de deserialización universal para Ruby 2.x–3.x desarrollado por vakzz, que permite la ejecución remota de comandos (RCE) en aplicaciones Ruby on Rails vulnerables. Este gadget será la base para construir nuestro objeto malicioso.

Solucion
interceptamos despues del login
![Pasted image 20250826232529.png](imagenes/Pasted image 20250826232529.png)
no copiamos la cookie en la termina y nos suelta info
![Pasted image 20250826232741.png](imagenes/Pasted image 20250826232741.png)
si buscamos mas info sobre esto (https://devcraft.io/2021/01/07/universal-deserialisation-gadget-for-ruby-2-x-3-x.html)
y alfinal de la pagina nos comparten un payload
![Pasted image 20250826233124.png](imagenes/Pasted image 20250826233124.png)
![Pasted image 20250826233154.png](imagenes/Pasted image 20250826233154.png)
tal que copiamos este codigo y lo modificamos
![Pasted image 20250826233628.png](imagenes/Pasted image 20250826233628.png)
pero si lo ejecutamos da problema por que la version que pide es un poco vieja por lo cual nos vamos apoyar de docker para ejecutar una version mas antigua
