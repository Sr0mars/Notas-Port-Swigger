Este laboratorio se centra en una vulnerabilidad XSS reflejada que, por sí sola, no es explotable en el navegador debido a que los caracteres especiales son codificados automáticamente en la barra de direcciones. Sin embargo, la clave está en cómo la caché normaliza las URLs.

Cuando se realiza una petición con una carga maliciosa en la ruta, la respuesta refleja directamente dicha ruta en el cuerpo. Aunque al acceder desde el navegador la carga se codifica y no se ejecuta, si previamente se ha hecho una petición idéntica desde Burp (sin codificación), la respuesta se almacena en la caché. Al visitar después esa misma URL desde el navegador (que codifica los caracteres especiales), la caché devuelve la versión previamente envenenada y el ‘**alert(1)**‘ se ejecuta con éxito en el navegador del usuario víctima.

Solucion
Interceptamos el home en BS
y en este caso se decofica el payload que tratamos de poner lo que hacemos es mandar el payload mientras esta cacheado accedemos a la url y le agregamos el script
![Pasted image 20250821223225.png](imagenes/Pasted image 20250821223225.png)
le damos send 
copiamos la url mas el payload
![Pasted image 20250821223310.png](imagenes/Pasted image 20250821223310.png)
y le damos ok
![Pasted image 20250821223338.png](imagenes/Pasted image 20250821223338.png)
