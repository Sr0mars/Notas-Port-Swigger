En esta clase damos el siguiente paso tras identificar el número de columnas: determinar cuál de esas columnas puede mostrar texto en la respuesta. Esto es necesario porque si intentamos inyectar una cadena en una columna que no admite texto, obtendremos un error.

La vulnerabilidad sigue estando en el filtro de categoría de productos, y como la respuesta de la aplicación muestra los resultados, podemos experimentar directamente.

El proceso es el siguiente:

- Primero se confirma cuántas columnas tiene la consulta, como ya se hizo en el laboratorio anterior.
- Luego se utiliza un valor aleatorio proporcionado por el propio laboratorio (como “abcdef”) y se prueba colocándolo en cada una de las posiciones ‘**NULL**‘ del payload, una a una.
- Si el valor aparece en la respuesta, significa que esa columna acepta datos tipo texto y puede usarse para mostrar información en futuras inyecciones.

Este paso es clave para que, en próximos ataques, podamos visualizar datos como nombres de usuarios, contraseñas, o cualquier otro campo sensible.

**Quédate con esto**: Saber qué columnas aceptan texto es imprescindible para extraer información visible mediante ataques UNION. Es un paso esencial en la preparación de una inyección efectiva.

Solucion 
primero el order by luego ponemos la cadena que nos esta pidiendo
