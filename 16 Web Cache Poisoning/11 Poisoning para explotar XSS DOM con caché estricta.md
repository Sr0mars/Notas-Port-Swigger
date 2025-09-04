En este laboratorio se explota una vulnerabilidad DOM-based XSS que no es directamente alcanzable por el atacante, pero que se puede activar mediante envenenamiento de caché. El desafío adicional es que el sistema de caché impone criterios estrictos, descartando por ejemplo las respuestas que contienen encabezados como ‘**Set-Cookie**‘.

El ataque se lleva a cabo manipulando el encabezado ‘**X-Forwarded-Host**‘ para que el script ‘**initGeoLocate()**‘ cargue un archivo JSON malicioso desde el exploit server, el cual contiene un payload que desencadena una ejecución de código en el navegador (por ejemplo, un ‘**alert(document.cookie)**‘). Para lograr que esta respuesta se almacene en la caché, se evita que el servidor incluya encabezados bloqueantes como Set-Cookie.

Una vez envenenada correctamente, la caché entrega el contenido malicioso a cualquier usuario que acceda a la página principal, logrando la ejecución del XSS en su navegador y resolviendo el laboratorio.

Solucion
como podemos ver en la web tenemos un apartado pasamos a inspeccionarlo
![Pasted_image_20250821223738.png](/Imagenes/Pasted_image_20250821223738.png)
y parece ser que es una imagen
![Pasted_image_20250821223842.png](/Imagenes/Pasted_image_20250821223842.png)
interceptamos el home
![Pasted_image_20250821224005.png](/Imagenes/Pasted_image_20250821224005.png)
podemos ver que en la seccion de codigo tenemos data el cual si filtramos data vemos que tiene una url
![Pasted_image_20250821224148.png](/Imagenes/Pasted_image_20250821224148.png)
si copiamos esta url y pegamos
vemos que viene la localizacion
![Pasted_image_20250821224238.png](/Imagenes/Pasted_image_20250821224238.png)
el cual se parece al que teniamos del carrito al principio
asi que ya que tenemos un exploit server pasamos a pegar la cabecera la cual nos ayudara a redirigirlo que en este caso es X-Forward-host:
![Pasted_image_20250821225311.png](/Imagenes/Pasted_image_20250821225311.png)
Modificamos el exploit conservamos el formato jason para que no se corrompa
![Pasted_image_20250821225328.png](/Imagenes/Pasted_image_20250821225328.png)
ya solo le damos send en el BS y recargamos la pagina
![Pasted_image_20250821225404.png](/Imagenes/Pasted_image_20250821225404.png)

