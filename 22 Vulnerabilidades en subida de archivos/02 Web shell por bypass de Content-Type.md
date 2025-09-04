En esta clase abordamos una funcionalidad de subida de archivos que intenta restringir los tipos de archivo permitidos mediante la verificación del encabezado Content-Type, el cual es manipulable por el usuario. Aprovechamos esta debilidad para modificar el valor del Content-Type en la solicitud HTTP y así engañar al sistema, logrando subir una shell PHP a pesar de las restricciones.

Una vez cargada, accedemos a ella directamente para ejecutar código en el servidor y leer archivos sensibles. Este laboratorio muestra cómo vulnerabilidades mal implementadas pueden ser explotadas incluso cuando existen controles superficiales.

Solucion
nos logeamos y vemos el mismo apartado de avatar si nosotro tratamos de subir el mismo archivo de shell nos saldra esto
esto es un content-type
![Pasted_image_20250830201234.png](Imagenes/Pasted_image_20250830201234.png)
![Pasted_image_20250830201334.png](Imagenes/Pasted_image_20250830201334.png)
si vemos en el historico vemos la solicitud post
![Pasted_image_20250830201656.png](Imagenes/Pasted_image_20250830201656.png)
lo mandamos al repeater y en el repeater podemos modificar el content
![Pasted_image_20250830201918.png](Imagenes/Pasted_image_20250830201918.png)
de tal manera que nos permite subir el archivo
de tal manera que si nosotros nos vamos al pagina y ponemos la direccion y el id podemos ver que se a subido
![Pasted_image_20250830202055.png](Imagenes/Pasted_image_20250830202055.png)
asi que ponemos la direccion
![Pasted_image_20250830202135.png](Imagenes/Pasted_image_20250830202135.png)
copiamos y pegamos
![Pasted_image_20250830202200.png](Imagenes/Pasted_image_20250830202200.png)
