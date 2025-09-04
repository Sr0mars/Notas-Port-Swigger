En esta clase nos enfrentamos a un sistema que valida minuciosamente los archivos subidos y elimina aquellos maliciosos tras realizar un análisis. Sin embargo, descubrimos una condición de carrera: existe una breve ventana de tiempo entre la subida del archivo y su análisis, durante la cual el archivo es accesible públicamente.

Aprovechamos esta situación para subir una shell PHP y realizar múltiples peticiones simultáneas que intentan acceder a ese archivo justo antes de que sea eliminado. Utilizamos Turbo Intruder para automatizar este ataque, combinando una solicitud POST con varias solicitudes GET inmediatas.

Esta técnica demuestra cómo los fallos en la gestión del tiempo y la concurrencia pueden abrir puertas incluso en sistemas con validaciones robustas.

Solucion
nos logeamos y subimos el archivo nos sale esto
![Pasted_image_20250830212622.png](Imagenes/Pasted_image_20250830212622.png)
nos vamos al historico y mandamos la peticion post al repeater
y bueno hay veces que el servidor se tarda un poco en dar la respues pues en ese breve tiempo nosotros podemos aprovecharnos para poder ver el archivo
de tal manera que generamos un peticion aun que no nos de respuesta
![Pasted_image_20250830213054.png](Imagenes/Pasted_image_20250830213054.png)
lo mandamos al repeater
agregamos las 2 y lo vamos a modificar con el send group (parallel)
![Pasted_image_20250830213205.png](Imagenes/Pasted_image_20250830213205.png)y vemos esto
![Pasted_image_20250830213324.png](Imagenes/Pasted_image_20250830213324.png)
asi que ahora ya solo modificamos la url 
![Pasted_image_20250830213529.png](Imagenes/Pasted_image_20250830213529.png)
Nota: el send se hace desde la pestaña 13
![Pasted_image_20250830213618.png](Imagenes/Pasted_image_20250830213618.png)
