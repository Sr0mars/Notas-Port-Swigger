En esta clase damos un paso más allá en el uso de técnicas fuera de banda para la explotación de inyecciones SQL ciegas. Aunque la consulta SQL se ejecuta de forma asíncrona y no afecta a la respuesta visible de la aplicación, es posible generar interacciones externas para exfiltrar información de forma pasiva.

La vulnerabilidad se encuentra nuevamente en la cookie ‘**TrackingId**‘, donde inyectamos un payload que construye dinámicamente una petición DNS hacia un subdominio de Burp Collaborator. En este caso, concatenamos la contraseña del usuario ‘**administrator**‘ dentro de la URL del dominio, de modo que dicha información se filtre al servidor externo.

El ataque utiliza funciones de XML como ‘**EXTRACTVALUE**‘ y el tipo ‘**xmltype**‘, combinadas con subconsultas SQL (**SELECT password FROM users WHERE username=’administrator’**) que inyectan el dato como parte de la resolución DNS.

Finalmente, desde la pestaña Collaborator de Burp Suite, verificamos las interacciones registradas y recuperamos el valor exfiltrado. Con esta contraseña accedemos como administrador y resolvemos el laboratorio.

Esta técnica resulta extremadamente eficaz en entornos donde no hay errores, ni cambios en el tiempo de respuesta ni retroalimentación alguna, aprovechando canales secundarios para obtener información confidencial del sistema.

Solucion
igual que los otros toca identificar el ataque dns para ver que BD es en cheet sheet pero esta funcion se ve en el BS collaborator
![Pasted_image_20250704143558.png](/Imagenes/Pasted_image_20250704143558.png)
![Pasted_image_20250704143738.png](/Imagenes/Pasted_image_20250704143738.png)
