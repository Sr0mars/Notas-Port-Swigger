Accedemos al código fuente desde la ruta ‘**/backup**‘ y analizamos la clase ‘**ProductTemplate**‘. Descubrimos que el método ‘**readObject()**‘ utiliza el campo **id** del objeto deserializado directamente en una consulta SQL, lo que introduce una inyección de SQL basada en objetos.

Creamos un pequeño programa en Java (o usamos la plantilla proporcionada) que serializa un objeto ‘ProductTemplate’ con un ID malicioso y lo convierte en una cadena Base64, lista para usar como cookie de sesión.

Solucion
nos logeamos e interceptamos
![Pasted_image_20250827000628.png](/Imagenes/Pasted_image_20250827000628.png)
vamos a la termina para ver que es
![Pasted_image_20250827000810.png](/Imagenes/Pasted_image_20250827000810.png)
vamos a ver el codigo fuente para ver si encontramos algo
![Pasted_image_20250827000852.png](/Imagenes/Pasted_image_20250827000852.png)
obtenemos una ruta vamos a ver que contiene
![Pasted_image_20250827000946.png](/Imagenes/Pasted_image_20250827000946.png)
¿Para qué sirve?
Este tipo de clase se usa para:
• 	Representar al usuario autenticado en una sesión.
• 	Transportar datos de autenticación entre capas de una aplicación.
• 	Guardar el estado del usuario en memoria, archivos o bases de datos.

hacemos directory listing
![Pasted_image_20250827002446.png](/Imagenes/Pasted_image_20250827002446.png)
y en el otro archivo encontramos esto
![Pasted_image_20250827002617.png](/Imagenes/Pasted_image_20250827002617.png)
Resumen 
• 	Representa un producto por su ID.
• 	Al deserializarse, se conecta a una base de datos PostgreSQL.
• 	Ejecuta una consulta SQL para recuperar los datos del producto.
• 	Si lo encuentra, reconstruye el objeto  desde el resultado.
• 	Usa  para gestionar la conexión.
• 	El campo  es , lo que significa que no se guarda al serializar, pero se reconstruye al deserializar.

En resumen: esta clase permite guardar solo el ID de un producto y luego recuperar sus datos completos desde la base de datos cuando se vuelve a cargar el objeto. Ideal para mantener objetos ligeros y conectados a datos dinámicos.

asi que vamos a crear un script en java pero aqui nos vamos apoyar de un repositorio de git (https://github.com/PortSwigger/serialization-examples/blob/master/java/solution/Main.java)
