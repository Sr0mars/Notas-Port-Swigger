En esta clase explotamos una vulnerabilidad de inyección SQL en un entorno Oracle, utilizando un ataque UNION para enumerar el contenido completo de la base de datos.

La vulnerabilidad se encuentra en el parámetro de categoría del filtro de productos, y la respuesta de la aplicación muestra los resultados de la consulta, lo que permite visualizar directamente los datos inyectados.

El objetivo es encontrar y consultar una tabla interna que almacena nombres de usuario y contraseñas. El proceso se desarrolla en varias fases:

- Identificar el número de columnas y las que permiten mostrar texto en la respuesta, utilizando un payload simple como prueba.
- Listar todas las tablas disponibles usando la vista ‘**all_tables**‘, propia de Oracle.
- Localizar la tabla de usuarios, observando los resultados devueltos por la consulta inyectada.
- Consultar ‘**all_tab_columns**‘ para descubrir los nombres de las columnas de esa tabla.
- Obtener los valores de usuario y contraseña realizando una consulta directa sobre la tabla objetivo.

Una vez localizada la contraseña del administrador, basta con iniciar sesión para resolver el laboratorio.

**Quédate con esto**: Aunque el sistema sea Oracle, los fundamentos de la inyección SQL siguen siendo aplicables. Lo importante es conocer las vistas internas adecuadas para cada motor de base de datos.
Solucion

En caso de que no funcione order by y sea oracle tenemos que utilizar el dual
![Pasted_image_20250702163506.png](/Imagenes/Pasted_image_20250702163506.png)
entonces para mostar la informacion de las tablas quitando el pet ' union select NULL,table_name from all_tables-- -
![Pasted_image_20250702163908.png](/Imagenes/Pasted_image_20250702163908.png)
vamos a extraer la infomacion de las columnas ' union select NULL,column_name from all_tab_columns where table_name='USERS_KILSBN'-- -
![Pasted_image_20250702164445.png](/Imagenes/Pasted_image_20250702164445.png)
ahora extraemos la informacion de los usuarios y contraseñas ' union select PASSWORD_HUFHYI,USERNAME_JGKXRW from USERS_KILSBN-- -
![Pasted_image_20250702164533.png](/Imagenes/Pasted_image_20250702164533.png)
nos logeamos 
![Pasted_image_20250702164619.png](/Imagenes/Pasted_image_20250702164619.png)
