En esta clase trabajamos con una aplicación vulnerable a server-side prototype pollution que intenta mitigar el problema filtrando directamente el uso de ‘**proto**‘. Sin embargo, descubrimos que es posible evadir esta protección inyectando propiedades maliciosas mediante la clave ‘**constructor.prototype**‘.

A través de esta vía logramos modificar propiedades heredadas en ‘**Object.prototype**‘. Verificamos la contaminación observando un cambio en la indentación del JSON de respuesta al establecer ‘**json spaces**‘, y luego identificamos un gadget útil: la propiedad ‘**isAdmin**‘. Al establecerla en true dentro del prototipo, conseguimos acceso al panel de administración y eliminamos al usuario Carlos.

Esta clase muestra cómo protecciones mal implementadas pueden ser burladas con técnicas alternativas, permitiendo comprometer el flujo de control de la aplicación.

Solucion
de igual manera nos logeamos y e interceptamos
![Pasted_image_20250901003333.png](Imagenes/Pasted_image_20250901003333.png)
y podemos ver que tenemos que convernirnos en admin
![Pasted_image_20250901003405.png](Imagenes/Pasted_image_20250901003405.png)
podemos tratar de cambiar la propiedad admin pero no funciona
![Pasted_image_20250901003622.png](Imagenes/Pasted_image_20250901003622.png)
vamos a tratar otra variables para ver si de esta forma podemos
![Pasted_image_20250901003827.png](Imagenes/Pasted_image_20250901003827.png)
en este caso vamos a tratar con constructor
,"constructor":{"prototype":{"isAdmin":true}}
![Pasted_image_20250901004256.png](Imagenes/Pasted_image_20250901004256.png)
ahora nos vamos a la pagina recargamos y eliminamos al usuario carlos
![Pasted_image_20250901004338.png](Imagenes/Pasted_image_20250901004338.png)
