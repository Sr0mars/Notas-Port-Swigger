En esta clase seguimos trabajando con XSS basado en DOM, esta vez enfocado en el uso inseguro de la propiedad que modifica directamente el contenido HTML de un elemento del DOM.

La aplicación vulnerable toma el valor introducido en la búsqueda (extraído directamente desde la URL) y lo inserta dentro del contenido de una etiqueta mediante una asignación directa sin aplicar ninguna medida de sanitización. Esto permite introducir fragmentos de código que se interpretan como HTML y que pueden incluir eventos maliciosos.

En este caso, se utiliza una imagen con una ruta inválida que provoca un error al cargar. Ese error activa un manejador de eventos que ejecuta el código malicioso, confirmando que la vulnerabilidad es explotable.

Esta lección refuerza el concepto de que, incluso sin interacción con el servidor, es posible comprometer a los usuarios si se procesan datos no confiables del lado cliente.

Solucion
Dentro de la pagina si le damos inspeccionar y buscamos hay un apartado de script
![Pasted_image_20250705155331.png](/Imagenes/Pasted_image_20250705155331.png)
Una de las opciones seria cargar una imagen
<img src=0 onerror=alert(0)>
![Pasted_image_20250705155912.png](/Imagenes/Pasted_image_20250705155912.png)
