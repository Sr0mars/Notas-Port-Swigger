Accedemos al contenido de ‘**Blog.php~**‘ y ‘**CustomTemplate.php~**‘, donde descubrimos una combinación peligrosa: **CustomTemplate** contiene un atributo ‘**template_file_path**‘ que apunta a un objeto **Blog**, y **Blog** tiene un atributo ‘**desc**‘ que se interpreta mediante el motor de plantillas Twig.

Además, el atributo **lockFilePath** se pasa a ‘**file_exists()**‘, lo cual es un vector común para disparar la deserialización PHAR. Esto nos permite preparar un objeto con un payload SSTI (Server-Side Template Injection) que se ejecutará al ser interpretado por Twig, combinando ambas técnicas para lograr RCE.

Solucion
en este caso la cookie de session no tiene deserilazacion por lo que pasamos a logearnos y explorar la pagina
![[Pasted image 20250827205719.png]]
y bueno lo que procede es subir una imagen y una vez subida inspeccionamos el codigo
vemos que tenemos una ruta
![[Pasted image 20250827210725.png]]
vamos a la ruta
![[Pasted image 20250827210910.png]]
tratamos de cambiar el usuario a carlos
![[Pasted image 20250827210940.png]]
si quitamos lo de avatar
![[Pasted image 20250827211110.png]]
tenemos una direccion
vamos a quitar avatar del todo
![[Pasted image 20250827211205.png]]
tenemos varios directorios
al tratar de abrirlos no podemos asi que usamos la tilde para poder acceder a los archivos
![[Pasted image 20250827211457.png]]
1.- Esta clase PHP permite leer y guardar archivos de plantilla de forma segura, usando un sistema de bloqueo basado en archivos . Así evita que se sobrescriba una plantilla mientras está en uso. Cuando el objeto se destruye, elimina el archivo de bloqueo automáticamente.
![[Pasted image 20250827211521.png]]
2.-Esta clase  permite representar un blog como un objeto que puede ser serializado/deserializado y convertido en cadena. Usa Twig para renderizar una plantilla con el contenido dinámico () y el nombre del usuario (). Al serializar el objeto, se excluye el motor Twig, y al deserializarlo, se reconstruye automáticamente.
![[Pasted image 20250827211809.png]]



