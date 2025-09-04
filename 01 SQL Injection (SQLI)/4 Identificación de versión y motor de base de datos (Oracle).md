En esta clase trabajamos con una inyección SQL más avanzada, en la que se utiliza la técnica de ataque UNION para combinar los resultados de la consulta original con una consulta manipulada por el atacante.

El objetivo es obtener información sobre la base de datos subyacente, concretamente el tipo de motor y su versión. En este caso, la base de datos es Oracle.

Para lograrlo:

- Se intercepta la solicitud que filtra los productos por categoría y se modifica el parámetro ‘category’.
- Primero se determina cuántas columnas devuelve la consulta y cuáles aceptan datos de tipo texto. Esto es necesario para que el ataque UNION funcione correctamente.
- Una vez identificadas las columnas, se utiliza una inyección que consulta la tabla ‘v$version’, propia de Oracle, para obtener el valor del campo ‘BANNER’, que contiene información sobre la versión de la base de datos.

Este tipo de ataque permite al atacante reconocer el entorno, lo que es clave para ajustar los siguientes pasos de explotación.

**Quédate con esto**: El ataque UNION es útil para extraer datos arbitrarios de la base de datos, y conocer el motor y versión es fundamental para planificar un ataque eficaz.

Pagina para ayudarte 
https://portswigger.net/web-security/sql-injection/cheat-sheet

![Pasted_image_20250701150253.png](/Imagenes/Pasted_image_20250701150253.png)
Solucion
' union select 'a',banner from v$version-- -
![Pasted_image_20250701150553.png](/Imagenes/Pasted_image_20250701150553.png)
