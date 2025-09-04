En esta lección abordamos una inyección SQL basada en errores visibles, donde la aplicación utiliza una cookie de seguimiento (**TrackingId**) en una consulta SQL sin validación adecuada. Mediante la manipulación de esta cookie, generamos errores intencionados que revelan fragmentos de la consulta interna.

Analizamos paso a paso cómo:

- Provocar un error de sintaxis añadiendo un carácter de comilla.
- Comentar el resto de la consulta para validarla sintácticamente.
- Utilizar subconsultas SQL combinadas con ‘**CAST**‘ para extraer información.
- Ajustar la consulta para obtener solo una fila y evitar errores de tipo.
- Filtrar primero el nombre de usuario del administrador y después su contraseña.

Finalmente, utilizamos la información exfiltrada para iniciar sesión como administrador, completando así con éxito el laboratorio.
Solucion 
primero la comilla en tracking id
![Pasted_image_20250703160109.png](/Imagenes/Pasted_image_20250703160109.png)
en BS vamos a realizar los demas pasos 
![Pasted_image_20250703160230.png](/Imagenes/Pasted_image_20250703160230.png)
lo siguiente seria usar cast para ver el error priviligeado
este puede ser uno usando limit
' or 1=cast((select username from users limit 1) as INT)-- -
![Pasted_image_20250703160821.png](/Imagenes/Pasted_image_20250703160821.png)
y lo mismo para la contraseña
' or 1=cast((select password from users limit 1) as INT)-- -
![Pasted_image_20250703160913.png](/Imagenes/Pasted_image_20250703160913.png)
