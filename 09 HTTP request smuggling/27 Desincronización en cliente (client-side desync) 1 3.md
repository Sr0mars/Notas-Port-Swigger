En esta primera parte analizamos el comportamiento del servidor ante longitudes de contenido manipuladas, y descubrimos que ignora el ‘**Content-Length**‘ en ciertas rutas, lo cual abre la puerta a un desync.

Confirmamos el vector mediante una secuencia de peticiones en Burp Repeater y luego replicamos ese comportamiento directamente desde el navegador utilizando ‘**fetch()**‘ con ‘**mode: cors**‘ y una cadena ‘**catch()**‘ para continuar la ejecución. Esto demuestra que el ataque es viable desde el cliente.

Solucion
![[Pasted image 20250812203604.png]]
Lo primero sera interceptar pero aqui se aplica un redirect hacia en pero lo quitamos y lo mandamos a la raiz
![[Pasted image 20250812204039.png]]
De primera se muestra un 302 asi que en este caso vamos a cambiar a post y mandarlo al http1
![[Pasted image 20250812204217.png]]
 vamos a empezar a probar cosas
 