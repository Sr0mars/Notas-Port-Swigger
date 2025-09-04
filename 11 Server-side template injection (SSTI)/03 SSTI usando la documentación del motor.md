En esta clase descubrimos una vulnerabilidad de SSTI aprovechando el motor de plantillas Freemarker. Analizando la documentación oficial, identificamos la función ‘**new()**‘ como vector de ataque para instanciar clases peligrosas, como **Execute**, que permite lanzar comandos del sistema.

Usamos este mecanismo para borrar un archivo dentro del servidor, demostrando cómo incluso las funciones documentadas pueden ser explotadas si no se restringen adecuadamente.

Solucion
entonces en esta parte nos pide que hagamos login una ves dentro miramos algun post y vemos que en la parte de abajo nos sale un tipo de codigo que tal parece ser que algo se esta cargando
![Pasted_image_20250814195445.png](/Imagenes/Pasted_image_20250814195445.png)
asi que vamos a forzar un error para ver a que nos estamos enfrentando
![Pasted_image_20250814195647.png](/Imagenes/Pasted_image_20250814195647.png)
asi que vamos a investigar
![Pasted_image_20250814195822.png](/Imagenes/Pasted_image_20250814195822.png)
aplicamos la de 3*3
![Pasted_image_20250814195911.png](/Imagenes/Pasted_image_20250814195911.png)
entonces ahora podemos aplicar codigo de ejecucion
![Pasted_image_20250814200139.png](/Imagenes/Pasted_image_20250814200139.png)
![Pasted_image_20250814200224.png](/Imagenes/Pasted_image_20250814200224.png)
