Este laboratorio expone una deserialización insegura en una aplicación Java que utiliza la librería Apache Commons Collections. Aunque no se tiene acceso al código fuente, es posible explotar la vulnerabilidad usando cadenas de gadgets preconstruidas.

Con la herramienta ‘**ysoserial**‘, se genera un objeto serializado con un payload que ejecuta un comando del sistema operativo para eliminar el archivo morale.txt de Carlos. Este objeto se inyecta en la cookie de sesión tras codificarlo adecuadamente.

Cuando el servidor deserializa el objeto, se desencadena la ejecución remota del comando. Este escenario representa una amenaza crítica frecuente en aplicaciones Java que confían en objetos serializados sin validación adecuada.

Solucion
![[Pasted image 20250826214508.png]]
entonces para ello nos vamos a apoyar de este recurso de git hub (https://github.com/frohoff/ysoserial/releases)
y vamos a seleccionar el archivo .jar
![[Pasted image 20250826214831.png]]
lo ejecutamos
![[Pasted image 20250826215143.png]]
y bueno aqui tenemos varios payloads
![[Pasted image 20250826215334.png]]
para que funcione primero necesitamos actualizar el java
![[Pasted image 20250826215605.png]]
en este caso vamos a utilizar el 1
pero no funciona asi que vamos a utilizar java 8 lo descargamos e instalamos
de tal manera que ya teniendolo vamosa ejecutar este comando (java -jar ysoserial-all.jar CommonsCollections4 'rm /home/carlos/morale.txt' | base64 -w 0; echo)
![[Pasted image 20250826222042.png]]
entonces ahora si vamos a interceptar despues de logearnos y lo mandamos al repeater  y quitamos la cookie y ponemos todo esta cadena aplicamos los cambios y copiamos el de arriba 
![[Pasted image 20250826223111.png]]
tal que con esto se soluciona el laboratorio
