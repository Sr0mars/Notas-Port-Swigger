Una vez subido el archivo avatar con el payload PHAR incrustado, realizamos una petición a ‘**avatar.php**‘ modificando el parámetro ‘**avatar**‘ para usar el protocolo ‘**phar://**‘.

Esto hace que ‘**file_exists()**‘ evalúe el archivo como un objeto serializado, desencadenando la ejecución de nuestro payload Twig embebido, lo cual provoca que se ejecute el comando ‘**rm /home/carlos/morale.txt**‘, resolviendo así el laboratorio.

Solucion
entonces una vez acabo el payload que daria asi
(<?php
    class Blog {}
    class CustomTemplate {}
    $blog = new Blog();
    $blog->user = 'pwned';                             
    $blog->desc = '{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("rm /home/carlos/morale.txt")}}';
    $obj = new CustomTemplate();
    $obj->template_file_path = $blog;
?>)

entonces para que funcione este codigo nosotro vamos a utilizar una herramienta en github que se llama polyglot (https://github.com/kunte0/phar-jpg-polyglot)
Este repositorio es una herramienta para generar archivos JPG que también contienen código PHAR ejecutable. Está pensado para pruebas de seguridad y retos CTF, y demuestra cómo una imagen aparentemente inocente puede ocultar código PHP malicioso. Es una técnica avanzada usada en auditorías de seguridad para detectar vulnerabilidades en el manejo de archivos por parte de aplicaciones PHP.
![[Pasted image 20250827214636.png]]
entonces modificamos el codigo de esta imagen
![[Pasted image 20250827214948.png]]
tal que vamos a elminar el ejemplo y poner nuestro codigo de archivo malicioso
![[Pasted image 20250827215132.png]]
tal que queda asi
![[Pasted image 20250827215341.png]]
ejecutamos pasandole los archivos
![[Pasted image 20250827215511.png]]
podemos ver que ya nos realiza el objeto
subimos el archivo out.jpg
![[Pasted image 20250827215629.png]]
vemos que la imagen se sube
![[Pasted image 20250827215724.png]]
si nosotros inspeccionamos la imagen vemos que tiene la misma ruta
![[Pasted image 20250827215807.png]]
copiamos solo que en este caso vamos agregar phar y le damos a enter
![[Pasted image 20250827215906.png]]vemos que nos sale not found pero si vamos al home
![[Pasted image 20250827215958.png]]
![[Pasted image 20250827220025.png]]
