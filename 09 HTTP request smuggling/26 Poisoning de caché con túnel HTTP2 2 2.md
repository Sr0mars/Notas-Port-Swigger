En esta segunda parte, pasamos de la exploración al ataque real: realizamos web cache poisoning utilizando un payload XSS inyectado a través de HTTP/2 request tunnelling. Ajustamos cuidadosamente el contenido para superar la longitud de la respuesta esperada y así evitar timeouts, asegurándonos de que el servidor refleje el código script alert(1) script sin codificar.

Una vez envenenada la caché, mantenemos el estado enviando solicitudes periódicas hasta que el usuario víctima accede a la home y ejecuta el script, resolviendo el laboratorio con éxito.

Solucion
por locual nos devuelve 2 estados 200
![Pasted_image_20250811194157.png](/Imagenes/Pasted_image_20250811194157.png)
entonces para resolver el laboratorio nosotros debemos poner mas cantidad de bytes que tiene la raiz 
![Pasted_image_20250812203210.png](/Imagenes/Pasted_image_20250812203210.png)
asi que nostros metemos la etique script y rellenamos los demas bytes con "A" de esta manera forzamos el error
![Pasted_image_20250812203315.png](/Imagenes/Pasted_image_20250812203315.png)
lo pegamos en el payload
![Pasted_image_20250812203353.png](/Imagenes/Pasted_image_20250812203353.png)
