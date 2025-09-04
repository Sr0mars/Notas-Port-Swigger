En esta clase nos centramos en el primer paso fundamental de un ataque SQL con UNION: determinar cuántas columnas devuelve la consulta original. Este paso es esencial para que el ataque funcione correctamente y no genere errores de sintaxis.

La aplicación presenta una inyección SQL en el filtro de categoría de productos. Como los resultados se reflejan en la respuesta, podemos usar esa ventaja para probar distintas combinaciones hasta que la estructura del ataque sea válida.

El proceso consiste en lo siguiente:

- Se intercepta la solicitud y se prueba un payload con ‘**UNION SELECT NULL**‘.
- Si el número de columnas no coincide, la base de datos devolverá un error.
- Se van añadiendo valores ‘**NULL**‘ separados por comas (por ejemplo, NULL, NULL, luego NULL, NULL, NULL, etc.) hasta que la respuesta deje de mostrar error y aparezca contenido nuevo.

Esto indica que el número de columnas del ‘**SELECT**‘ inyectado coincide con el de la consulta original, y ya es posible construir ataques UNION funcionales para extraer datos reales.

**Quédate con esto**: Un ataque UNION solo funciona si el número y tipo de columnas coinciden. Identificar correctamente esta estructura es el primer paso para una explotación exitosa.

Solucion
primero el order by y luego esto
![Pasted_image_20250702165201.png](Imagenes/Pasted_image_20250702165201.png)
