En esta clase trabajamos con un XSS reflejado que no ocurre dentro del cuerpo de una etiqueta HTML, sino dentro de un atributo. La aplicación codifica los signos angulares para evitar que se abran etiquetas directamente, pero permite inyectar contenido dentro de valores entre comillas.

La funcionalidad vulnerable es el buscador del blog. Al introducir un valor en el cuadro de búsqueda, este se refleja dentro de un atributo HTML en la respuesta. Usando herramientas como Burp Suite, interceptamos la petición y comprobamos que nuestro valor aparece entre comillas dentro de ese atributo.

La estrategia consiste en cerrar el valor actual del atributo e introducir uno nuevo que contenga un manejador de eventos (por ejemplo, uno que se active al pasar el ratón). Al acceder a la URL modificada y mover el cursor sobre el área afectada, se ejecuta el código inyectado, demostrando que la inyección fue exitosa.

Este laboratorio destaca la importancia de validar correctamente no solo el contenido de las etiquetas, sino también lo que va dentro de atributos, donde también es posible ejecutar código si no se sanitiza correctamente.

Solucion 
Basicamente nos aprovechamos de las comillas que hacen falta y probamos codigo
![Pasted_image_20250707155745.png](Imagenes/Pasted_image_20250707155745.png)
Lo que aqui pasa es que sierra la doble comilla que en un principio estaba abierta esto hace que podamos probar codigo xss
"test=probando"
![Pasted_image_20250707160034.png](Imagenes/Pasted_image_20250707160034.png)
ahora podemos utilizar esta sentencia para poder ver el mensaje "onmouseover="alert(0)
![Pasted_image_20250707160256.png](Imagenes/Pasted_image_20250707160256.png)
Lo que hace es que al pasar el mouse nos muestra la pantalla de mensaje
