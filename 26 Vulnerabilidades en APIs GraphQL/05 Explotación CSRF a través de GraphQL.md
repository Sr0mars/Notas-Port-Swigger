En esta clase explotamos una vulnerabilidad de CSRF en una API GraphQL que permite ejecutar mutaciones autenticadas desde otro sitio web. Observamos que el cambio de correo se realiza mediante una mutación enviada como JSON, pero el servidor también acepta el tipo de contenido ‘**x-www-form-urlencoded**‘.

Convertimos la mutación a este formato y confirmamos que sigue funcionando correctamente al reutilizar la cookie de sesión. Usamos Burp Suite para generar un HTML malicioso que envía esta petición al servidor de forma automática cuando un usuario autenticado visita la página. Subimos este código al exploit server y lo entregamos a la víctima para cambiar su correo sin interacción explícita.

Esta clase demuestra cómo los ataques CSRF también pueden aplicarse en entornos GraphQL si no se implementan medidas de protección como tokens anti-CSRF o verificación del origen.

Solucion
nos logeamos y de momento el campo que nos interesa es el actualizar el correo tal que ese lo interceptamos tambien podemos ver que nos comparten un exploit server
![Pasted image 20250901030246.png](imagenes/Pasted image 20250901030246.png)
aqui la idea es cambiar el content tipe para que no lo mande a nuestro exploit server
![Pasted image 20250901030517.png](imagenes/Pasted image 20250901030517.png)
importante copiarnos la query es posible que se elimine
({"query":"\n    mutation changeEmail($input: ChangeEmailInput!) {\n        changeEmail(input: $input) {\n            email\n        }\n    }\n","operationName":"changeEmail","variables":{"input":{"email":"test@test.com"}}})
como la modifique
(query=\n    mutation changeEmail($input: ChangeEmailInput!) {\n        changeEmail(input: $input) {\n            email\n        }\n    }\n&operationName&changeEmail&variables={"input":{"email":"test@test.com"}})
![Pasted image 20250901031911.png](imagenes/Pasted image 20250901031911.png)
ahora le damos click derecho y vamos a cambiar el metodo esto lo hacemos 2 veces para que nos aparesca el content type
![Pasted image 20250901030802.png](imagenes/Pasted image 20250901030802.png)
tal que ahora la query le tenemos que representar en formato json por lo cual hacemos lo siguiente
cat data | sed 's/\\n/%0A/g' | sed 's/ /+/g'
![Pasted image 20250901031252.png](imagenes/Pasted image 20250901031252.png)
y aqui ya me lo acepta
![Pasted image 20250901032104.png](imagenes/Pasted image 20250901032104.png)
y ahora lo mandamos a formato poc y lo pegamos en el exploit server y lo mandamos a la victima

