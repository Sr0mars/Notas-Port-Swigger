En esta clase exploramos una vulnerabilidad que combina la subida de archivos con un fallo de path traversal. Aunque el servidor restringe la ejecución de archivos subidos en el directorio por defecto, conseguimos evadir esta medida modificando el nombre del archivo mediante secuencias de directorios relativas, como ‘**../**‘, codificadas en URL.

De este modo, logramos que el archivo se guarde fuera del entorno restringido, en una ruta ejecutable. Una vez allí, accedemos a nuestra shell PHP desde el navegador y extraemos el contenido del archivo secreto de Carlos. Esta técnica demuestra cómo vulnerabilidades combinadas pueden romper medidas de protección que, por sí solas, serían efectivas.

Solucion
volvemos a logearnos y subimos el archivo
![Pasted image 20250830202421.png](imagenes/Pasted image 20250830202421.png)
al parecer se a subido vamos al la ruta
![Pasted image 20250830202507.png](imagenes/Pasted image 20250830202507.png)
y parece que no me interpreta el codigo php
y nos vamos otra vez al historico y vemos la ultima peticion post donde nos interpreta el archivo y lo mandamos al repeater
![Pasted image 20250830202809.png](imagenes/Pasted image 20250830202809.png)
y lo que podemos hacer es retroceder algunos directorios para ver si me permite subir el archivo
![Pasted image 20250830203008.png](imagenes/Pasted image 20250830203008.png)
vemos que no me lo interpreta vamos a urldearlo
![Pasted image 20250830203056.png](imagenes/Pasted image 20250830203056.png)
y parece que me lo ha subido un directorio atras
![Pasted image 20250830203135.png](imagenes/Pasted image 20250830203135.png)
por lo cual se supone que me lo ha subido
![Pasted image 20250830203229.png](imagenes/Pasted image 20250830203229.png)
por lo cual ingresamos a la ruta y vemos la secret
![Pasted image 20250830203335.png](imagenes/Pasted image 20250830203335.png)
copiamos y pegamos en la web
![Pasted image 20250830203422.png](imagenes/Pasted image 20250830203422.png)
