En esta clase exploramos cómo es posible realizar un ataque de Web Cache Poisoning al manipular el comportamiento del servidor frente a peticiones ambiguas, concretamente aquellas con múltiples cabeceras Host.

El laboratorio demuestra que el servidor ignora la segunda cabecera Host a la hora de validar la petición, pero aún así refleja su valor en la respuesta dentro de una URL absoluta para cargar un script (**/resources/js/tracking.js**). Esta diferencia de interpretación entre el sistema de caché y el back-end permite que un atacante almacene en caché una versión maliciosa de la página, que luego será servida a otros usuarios.

El atacante almacena en su servidor una versión maliciosa de ‘**tracking.js**‘ que ejecuta ‘**alert(document.cookie)**‘. Luego, mediante Burp Repeater, envía una petición con dos cabeceras Host: una válida para que la caché acepte la respuesta y otra apuntando a su servidor. Al forzar múltiples peticiones con distintos parámetros (**?cb=123**, etc.), consigue que el contenido envenenado se almacene en la caché.

Cuando el usuario víctima accede a la home, el navegador carga el script desde el servidor del atacante, ejecutando el payload JavaScript. La clase enseña cómo aprovechar una discrepancia sutil entre la caché y el servidor para inyectar contenido malicioso, algo especialmente peligroso en sitios de alto tráfico.

Solucion
vamos a interceptar el home y lo mandamos al repeater de igual manera nos comparten un exploit server
![Pasted_image_20250829202656.png](Imagenes/Pasted_image_20250829202656.png)
lo primero seria revisar si se puede refrescar la cache de la pagina
![Pasted_image_20250829202827.png](Imagenes/Pasted_image_20250829202827.png)
podemos notar que si por que en el age se mantiene a 0
entonces lo que podemos hacer es meter otro host y poner un test para ver si en la respuesta vemos algo
![Pasted_image_20250829203218.png](Imagenes/Pasted_image_20250829203218.png)
y esto si lo vemos y podemos ver el recurso de js/tracking
por lo cual en el exploit server tocaria modificarlo
![Pasted_image_20250829203545.png](Imagenes/Pasted_image_20250829203545.png)
y en BS quedaria asi
![Pasted_image_20250829203617.png](Imagenes/Pasted_image_20250829203617.png)
y cuando recargamos la pagina podemos ver que sea resuelto
![Pasted_image_20250829203808.png](Imagenes/Pasted_image_20250829203808.png)


