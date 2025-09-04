En esta clase aprovechamos una mala implementación del control de acceso en un endpoint GraphQL que gestiona usuarios. Mediante una introspection query descubrimos una consulta llamada ‘**getUser**‘ que permite obtener directamente el nombre de usuario y la contraseña asociados a un ID.

Al probar distintos valores de ID, identificamos que el usuario administrador tiene el ID 1, y logramos extraer sus credenciales directamente desde la API. Con estos datos accedemos como administrador y eliminamos al usuario carlos.

Esta clase muestra cómo una exposición accidental de campos internos en GraphQL puede poner en riesgo cuentas críticas si no se aplican restricciones estrictas a las consultas y a los datos retornados.

Solucion
entramos a la pagina vemos en el historico que existe un graph lo mandamos al repeater
![Pasted_image_20250901015349.png](Imagenes/Pasted_image_20250901015349.png)
y bueno vamos a verificar si es vulnerable 
![Pasted_image_20250901015537.png](Imagenes/Pasted_image_20250901015537.png)nos da mucha informacion vamos a tratar de acomodarlo
![Pasted_image_20250901015634.png](Imagenes/Pasted_image_20250901015634.png)
nos vamos al site map y por la url del laboratorio filtramos
![Pasted_image_20250901015815.png](Imagenes/Pasted_image_20250901015815.png)
y vamos desplegando hasta que nos sale uno de getUser esto lo mandamos al repeater
y como podemos ver arriba tiene un identificador si cambiamos ese identificador
![Pasted_image_20250901015952.png](Imagenes/Pasted_image_20250901015952.png)
nos dal la contraseña del usuario admin
y ya con ese nos logeamos accedemos al admin panel y eliminamos al usuario carlos
![Pasted_image_20250901020052.png](Imagenes/Pasted_image_20250901020052.png)

