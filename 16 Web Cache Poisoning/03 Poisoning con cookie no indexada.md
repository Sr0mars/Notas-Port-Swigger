En este laboratorio exploramos un escenario en el que la cookie ‘**fehost**‘, enviada por el cliente y reflejada en la respuesta del servidor, no se utiliza como parte de la clave de caché. Esto significa que es posible modificar su valor para introducir un payload malicioso, como un ‘**alert(1)**‘, y lograr que la respuesta sea cacheada con ese contenido.

Tras identificar esta condición, se utiliza una cadena especialmente construida en la cookie para romper la estructura original de la respuesta e insertar el script. Luego, al comprobar que la respuesta manipulada es almacenada en caché (**X-Cache: hit**), se espera a que un usuario desprevenido acceda a la página y ejecute el payload.

Este ejercicio demuestra cómo una cookie mal gestionada puede abrir la puerta a ataques de Web Cache Poisoning con impacto directo en el navegador de las víctimas.

Solucion
y bueno repetimos los pasos mandamos la pagina principal al repeter
![Pasted_image_20250821202921.png](/Imagenes/Pasted_image_20250821202921.png)
si nosotro queremos que se reinicie la cache basta con poner en la parte del directorio ?test=1
asi que en este punto nosotro podemos controlar en la parte de javascript el codigo con la opcion de fehost
![Pasted_image_20250821203325.png](/Imagenes/Pasted_image_20250821203325.png)
asi que para manipular esto nosotro lo que podemos hacer es cerrar con doble " por que es codigo javascript (mandamos una alerta) hacia la raiz
![Pasted_image_20250821203534.png](/Imagenes/Pasted_image_20250821203534.png)
y ya recargamos la pagina
![Pasted_image_20250821203630.png](/Imagenes/Pasted_image_20250821203630.png)
