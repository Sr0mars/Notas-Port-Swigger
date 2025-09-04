En esta clase abordamos una variante de XXE ciega que se apoya en mensajes de error para filtrar información sensible. Continuamos aprovechando el sistema de entidades parametrizadas, pero en lugar de usar canales externos como Collaborator, utilizamos rutas inválidas para provocar errores intencionados que revelen el contenido del archivo /etc/passwd.

Preparamos una DTD maliciosa en nuestro exploit server que lee ese archivo y lo introduce como parte de una ruta errónea. Al invocar esa DTD desde el XML enviado al endpoint vulnerable, el servidor intenta acceder a una ruta inválida que incluye el contenido del archivo, lo que provoca un error con el texto completo de la entidad.

Analizamos cómo estructurar correctamente tanto la DTD como el XML final y validamos el resultado observando la aparición del archivo dentro del mensaje de error devuelto. Esta técnica demuestra cómo aprovechar los errores internos del servidor como canal de exfiltración en ataques ciegos.

Solucion
Lo que se realizo como el anterior laboratorio fue poner esto en nuestro exploit server
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'file:///invalid/%file;'>">
%eval;
%exfil;

y lo que pusimos en el BS fue esto sin modificar nada dentro del xml
![Pasted_image_20250730203420.png](/Imagenes/Pasted_image_20250730203420.png)

