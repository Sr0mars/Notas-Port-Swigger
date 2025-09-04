Modificamos el script del gadget encontrado para que ejecute ‘**rm /home/carlos/morale.txt**‘, y adaptamos su salida para que genere el objeto en formato Base64.

Este objeto se inserta en la cookie de sesión y se codifica en URL antes de ser enviado al servidor.

El backend deserializa el objeto malicioso y ejecuta el comando, eliminando el archivo y resolviendo el laboratorio.

Solucion
asi que aqui installamos ruby con docker
![Pasted image 20250826234557.png](imagenes/Pasted image 20250826234557.png)
ahora aqui creamos el mismo archivo y lo ejecutamos
pero como lo queremos en base64 vamos a modificarlo (es encode)
![Pasted image 20250826235142.png](imagenes/Pasted image 20250826235142.png)
tal que quedaria asi
![Pasted image 20250826235248.png](imagenes/Pasted image 20250826235248.png)
por ultimo sacamos los saltos de linea
![Pasted image 20250826235421.png](imagenes/Pasted image 20250826235421.png)
copiamos y pegamos la coockie en el navegador
![Pasted image 20250826235516.png](imagenes/Pasted image 20250826235516.png)
![Pasted image 20250826235544.png](imagenes/Pasted image 20250826235544.png)
