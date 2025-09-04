En esta clase comprobamos cómo el parámetro de búsqueda de usuario en MongoDB es vulnerable a inyección NoSQL. Partimos de errores sintácticos y los transformamos en expresiones booleanas como **‘ && ‘1’==’1** que nos permiten verificar si el servidor evalúa condiciones.

Esto nos da la capacidad de generar respuestas diferentes según si la condición inyectada es verdadera o falsa, base fundamental para extraer datos sensibles de forma estructurada.

Solucion
y nos logeamos y cuando intentamos recargar la pagina se nota que se tarda un poco esto puede ser por uqe esta viniendo de otro lado
![Pasted_image_20250902004905.png](Imagenes/Pasted_image_20250902004905.png)
si nos vamos al historico vemos que venia de lookup esto lo mandamos al repeater
![Pasted_image_20250902004949.png](Imagenes/Pasted_image_20250902004949.png)
![Pasted_image_20250902005208.png](Imagenes/Pasted_image_20250902005208.png)
![Pasted_image_20250902005522.png](Imagenes/Pasted_image_20250902005522.png)
¿Qué significa ?
En muchos lenguajes de consulta NoSQL (como MongoDB o algunas implementaciones de JavaScript en el backend), los operadores lógicos como  (OR) pueden ser interpretados directamente si no hay una validación adecuada.
Lo que hace es forzar la condición a ser siempre verdadera, porque (true) es una constante booleana que no depende de ningún dato real. Si el backend no valida correctamente el parámetro user , puede terminar ejecutando algo como: db.users.find({ user: '' || true || '' })
![Pasted_image_20250902005655.png](Imagenes/Pasted_image_20250902005655.png)
¿Por qué te devolvió info del administrador?
Porque al hacer que la condición sea siempre verdadera, el servidor probablemente respondió con el primer usuario en la base de datos, que suele ser el administrador o un usuario con privilegios.

⚠️ ¿Qué implica esto?
• 	El sistema es vulnerable a NoSQL Injection.
• 	No está validando ni sanitizando los parámetros de entrada.
• 	Podrías usar esta técnica para extraer más datos, modificar registros o incluso escalar privilegios si el backend lo permite.

Esto basicamente lo que nos confirma es que hay una NOsql
