En esta segunda parte del laboratorio, aprovechamos la vulnerabilidad de XSS almacenado que identificamos previamente para robar la cookie persistente de Carlos. Insertamos un payload malicioso en los comentarios del blog, el cual fuerza al navegador de Carlos a enviar su cookie al servidor de explotación que controlamos.

Una vez obtenida la cookie, la decodificamos y extraemos el hash MD5 de la contraseña. Como es una contraseña débil, se puede crackear fácilmente con herramientas como Hashcat o incluso usando motores de búsqueda.

Con la contraseña descubierta, iniciamos sesión como Carlos y procedemos a eliminar su cuenta desde el panel de usuario, completando así con éxito el laboratorio.

Solucion
entonce la idea es le damos a publicar el post despues pasamos hacia los logs y nos an dejado una cadena
![Pasted_image_20250820215804.png](Imagenes/Pasted_image_20250820215804.png)
vamos a desglozar para ver que es esto
![Pasted_image_20250820220017.png](Imagenes/Pasted_image_20250820220017.png)
ahora para ver que es utilizamos una pagina llamada hashes.com
copiamos la contraseña
![Pasted_image_20250820220229.png](Imagenes/Pasted_image_20250820220229.png)
y ahora nos logeamos con la cuenta de carlos poniendo esta posible contraseña
![Pasted_image_20250820220337.png](Imagenes/Pasted_image_20250820220337.png)
![Pasted_image_20250820220413.png](Imagenes/Pasted_image_20250820220413.png)
