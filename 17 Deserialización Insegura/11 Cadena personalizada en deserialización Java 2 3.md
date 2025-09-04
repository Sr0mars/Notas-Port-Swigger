En lugar de recompilar manualmente el código Java para cada payload, aprovechamos Hackvertor para probar múltiples cargas útiles directamente desde Burp.

Trabajamos sobre una plantilla de objeto que permite insertar payloads SQL fácilmente, manteniendo la estructura del objeto válida y actualizando las longitudes automáticamente.

Esto nos permite realizar inyecciones tipo UNION para descubrir el número de columnas y qué campos aceptan cadenas, preparando el camino para la extracción de datos.

Solucion
no lo copiamos
![Pasted_image_20250827004452.png](/Imagenes/Pasted_image_20250827004452.png)
y ahora nos copiamos esto en una nuevo archivo (https://github.com/PortSwigger/serialization-examples/blob/master/java/solution/data/productcatalog/ProductTemplate.java) que sera el template
y este que sera el product (https://github.com/PortSwigger/serialization-examples/blob/master/java/solution/data/productcatalog/Product.java)
![Pasted_image_20250827005134.png](/Imagenes/Pasted_image_20250827005134.png)
asi que para que funcione nos cambiamos de version
a la 17
![Pasted_image_20250827005708.png](/Imagenes/Pasted_image_20250827005708.png)
entonces pasamos a ejecutarlo
![Pasted_image_20250827005930.png](/Imagenes/Pasted_image_20250827005930.png)
si esto lo sustituimos
![Pasted_image_20250827005959.png](/Imagenes/Pasted_image_20250827005959.png)
en base a este error ahora podemos probar consultas de sql
![Pasted_image_20250827010746.png](/Imagenes/Pasted_image_20250827010746.png)
entonces sustituimos la coockie que nos da en el request
![Pasted_image_20250827011031.png](/Imagenes/Pasted_image_20250827011031.png)
y obtenemos un error es posible que alla funcionado
![Pasted_image_20250827011011.png](/Imagenes/Pasted_image_20250827011011.png)
probamos de esta manera
![Pasted_image_20250827011145.png](/Imagenes/Pasted_image_20250827011145.png)
