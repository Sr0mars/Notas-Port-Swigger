En esta primera parte, analizamos cómo la combinación del pseudo-header ‘**:path**‘ en HTTP/2 y el proceso de downgrade a HTTP/1.1 permite inyectar cabeceras y peticiones completas a través de request tunnelling. Probamos diferentes vectores utilizando el parámetro ‘**cachebuster**‘ para evitar respuestas en caché y comprobar visualmente el contenido de las respuestas inyectadas.

Con esto, conseguimos verificar que podemos modificar la caché del sistema, sentando las bases para el ataque de XSS persistente en la segunda parte.

Solucion
Empezamos a interceptar el home
![Pasted_image_20250811185739.png](Imagenes/Pasted_image_20250811185739.png)
empezamos con las consultas en este caso como es http2 no se aplican lo de las cabeceras
![Pasted_image_20250811185905.png](Imagenes/Pasted_image_20250811185905.png)
pero no obtenemos nada vamos a meter el payload en el name para ver si es vulnerable
![Pasted_image_20250811190020.png](Imagenes/Pasted_image_20250811190020.png)
Pero tampoco funciona
pero podemos probar con cabeceras ya establecidas como seria el path
![Pasted_image_20250811190302.png](Imagenes/Pasted_image_20250811190302.png)
si probamos con una ruta esto puede ser una entrada a tomar encuenta
![Pasted_image_20250811190457.png](Imagenes/Pasted_image_20250811190457.png)Entonces probando rutas nos encontramos con un proxy error lo cual deriba que sea por el tamaño de bytes
![Pasted_image_20250811191228.png](Imagenes/Pasted_image_20250811191228.png)
![Pasted_image_20250811191248.png](Imagenes/Pasted_image_20250811191248.png)
entonces que tenemos que hacer aqui 
necesitmaos buscar una ruta en donde la consulta nos permetima ver mas por la cantidad de bytes que estan
![Pasted_image_20250811191541.png](Imagenes/Pasted_image_20250811191541.png)
en este caso podemos ver que el post 2 tiene menos cantidad de bytes enfrente al post 4
de esta manera quedaria la consulta
![Pasted_image_20250811191657.png](Imagenes/Pasted_image_20250811191657.png)
