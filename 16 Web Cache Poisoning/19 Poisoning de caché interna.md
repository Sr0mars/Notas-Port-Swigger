Este laboratorio presenta una configuración compleja con múltiples capas de caché. La clave está en entender que la caché externa sí toma en cuenta los parámetros de la URL y ciertos encabezados como ‘**X-Forwarded-Host**‘, pero la caché interna no lo hace.

Esto permite envenenar de forma aislada fragmentos individuales de la página, como el recurso ‘geolocate.js’, aprovechando que su URL se construye dinámicamente con el valor del encabezado ‘**X-Forwarded-Host**‘.

A través de múltiples peticiones con y sin ‘**cache buster**‘, se comprueba que el recurso ‘**geolocate.js**‘ mantiene la versión manipulada incluso cuando otros elementos se restauran, revelando que se encuentra cacheado de forma separada.

Una vez identificado, se reemplaza este archivo con una versión maliciosa desde el servidor de explotación y se aprovecha la desincronización entre las capas de caché para hacer que el navegador de la víctima cargue el script modificado, logrando así ejecutar ‘**alert(document.cookie)**‘ en su entorno.

Esta técnica demuestra cómo una configuración aparentemente segura puede ser vulnerada si existen diferencias en el comportamiento entre las distintas capas de caché.

Solucion
bueno interceptamos la raiz y podemos ver que en script vemos 2 localizaciones
![Pasted_image_20250822205503.png](/Imagenes/Pasted_image_20250822205503.png)
esta es la de analitics
![Pasted_image_20250822205534.png](/Imagenes/Pasted_image_20250822205534.png)
esta es la de geolocate
![Pasted_image_20250822205606.png](/Imagenes/Pasted_image_20250822205606.png)
entonces podemos utilizar la cabecera X-Forwarded-Host:
y como nos comparte el exploit server podemos probar con uno de los src
en este caso empleamos el de js/geolocate.js
![Pasted_image_20250822211126.png](/Imagenes/Pasted_image_20250822211126.png)
y bueno la siguiente parte es spamear hasta que en los 2 salga exploit server 
esto seria el antes
![Pasted_image_20250822211053.png](/Imagenes/Pasted_image_20250822211053.png)
y esto tendria que salir despues de spamear bastante
![Pasted_image_20250822210941.png](/Imagenes/Pasted_image_20250822210941.png)y ya solo recargamos la pagina
![Pasted_image_20250822211225.png](/Imagenes/Pasted_image_20250822211225.png)
