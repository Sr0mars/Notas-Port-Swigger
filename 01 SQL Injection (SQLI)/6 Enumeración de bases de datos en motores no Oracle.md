En esta clase realizamos una inyección SQL avanzada en bases de datos que no son Oracle, utilizando el ataque UNION para enumerar tablas, columnas y extraer información sensible.

La vulnerabilidad está en el parámetro de categoría de productos. Gracias a que la respuesta incluye los datos de la consulta, podemos aprovecharla para visualizar información del sistema.

El objetivo final es extraer las credenciales de todos los usuarios (incluido el administrador) a partir de las siguientes etapas:

- Descubrir cuántas columnas devuelve la consulta original y qué tipo de datos aceptan, usando un payload simple para comprobarlo.
- Listar todas las tablas existentes en la base de datos consultando ‘**information_schema.tables**‘, una tabla especial que contiene metadatos.
- Identificar la tabla que almacena los usuarios y contraseñas, observando su nombre en la respuesta.
- Listar las columnas de esa tabla, consultando ‘**information_schema.columns**‘ y filtrando por el nombre de tabla que acabamos de encontrar.
- Extraer los valores de las columnas relevantes, mostrando directamente los nombres de usuario y contraseñas de todos los usuarios.

Una vez obtenida la contraseña del administrador, podemos usarla para iniciar sesión en la aplicación y completar el laboratorio.

**Quédate con esto**: Con técnicas de enumeración y ataques UNION bien estructurados, es posible reconstruir la estructura interna de una base de datos y acceder a información crítica como credenciales de usuarios.

Solucion hacemos los mismo pasos que en el otro paso pero en este punto tenemos que tener cuidado con group ya que no funciona aveces por lo que solo podemos utilizar concat
![Pasted_image_20250702161452.png](/Imagenes/Pasted_image_20250702161452.png)
tenemos que tener cuidado con las comillas
![Pasted_image_20250702161741.png](/Imagenes/Pasted_image_20250702161741.png)
ya que tenemos identificada la tabla solo falta hacerle la consulta ' union select NULL,column_name from information_schema.columns where table_schema='public' and table_name='users_iyelfy'-- -
![Pasted_image_20250702162102.png](/Imagenes/Pasted_image_20250702162102.png)
![Pasted_image_20250702162239.png](/Imagenes/Pasted_image_20250702162239.png)
![Pasted_image_20250702162323.png](/Imagenes/Pasted_image_20250702162323.png)
