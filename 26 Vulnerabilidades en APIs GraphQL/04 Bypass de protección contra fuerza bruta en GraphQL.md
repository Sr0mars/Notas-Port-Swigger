En esta clase aprovechamos una debilidad en la implementación del rate limiting de un endpoint GraphQL. Aunque el servidor bloquea múltiples intentos de login si llegan rápidamente desde una misma fuente, descubrimos que es posible evadir esta protección utilizando la funcionalidad de aliases de GraphQL.

En lugar de enviar una petición por intento, agrupamos decenas de intentos en una sola mutación compuesta, cada una con un alias único y una contraseña distinta. Esto nos permite realizar un ataque de fuerza bruta efectivo sin activar el sistema de rate limiting. Al recibir la respuesta, buscamos cuál de las mutaciones fue exitosa, extraemos la contraseña correcta y accedemos como el usuario carlos.

Esta clase demuestra cómo el conocimiento del comportamiento interno de GraphQL puede usarse para sortear medidas de seguridad superficiales.

Solucion
lo primero es que nos comparten unas contraseñas
![Pasted image 20250901022349.png](imagenes/Pasted image 20250901022349.png)
asi que no nos dan credenciales por lo que navegamos en la web checamos en el historico
![Pasted image 20250901022515.png](imagenes/Pasted image 20250901022515.png)
vemos un graphql lo mandamos al repeater
vamos a darle click derecho y ponemos el set introspection
![Pasted image 20250901022632.png](imagenes/Pasted image 20250901022632.png)ahora lo mandamos al site map
![Pasted image 20250901022740.png](imagenes/Pasted image 20250901022740.png)
y de lo que vemos algo que nos podria interesar es el login que se muestra lo mandamos al repeater
![Pasted image 20250901022902.png](imagenes/Pasted image 20250901022902.png)
y bueno probamos el usuario carlos con x contraseña pero no nos da respuesta (false)
![Pasted image 20250901023119.png](imagenes/Pasted image 20250901023119.png)
asi que algo que podemos hacer es dentro de la query modificarla
de tal manera que podemos ir probando de es manera las contraseñas
![Pasted image 20250901023754.png](imagenes/Pasted image 20250901023754.png)
asi que como tenemos un diccionario vamos a crearnos un payload en bash llamado generator.sh
(#!/bin/bash

text='''
intento_x: login(input: {username: "carlos", password: "omar"}) {\n
\ttoken\n
\tsuccess\n
}
'''
counter=1
cat passwords | while read password; do
  echo -e $text | sed "s/omar/$password/" | sed "s/intento_x/intento_$counter/"

  let counter+=1
done)

nos entrega esto
![Pasted image 20250901025537.png](imagenes/Pasted image 20250901025537.png)
y ya solo copiamos y pegamos en la query y filtramos por true vemos que es el intento 53 lo buscamos en el  request y vemos que es ranger
![Pasted image 20250901025655.png](imagenes/Pasted image 20250901025655.png)
y ya solo nos logeamos
![Pasted image 20250901025803.png](imagenes/Pasted image 20250901025803.png)
