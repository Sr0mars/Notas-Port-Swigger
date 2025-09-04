En esta clase exploramos cómo rutas expuestas en ‘**robots.txt**‘ pueden revelar directorios sensibles como ‘**/backup**‘. Al acceder a un archivo ‘**.java.bak**‘ dentro de esta ruta, obtenemos acceso al código fuente de la aplicación. Dentro de este archivo, identificamos una cadena hardcoded con la contraseña de acceso a la base de datos PostgreSQL, con la cual completamos el laboratorio.

Solucion
bueno nosotros ocupamos la ruta robots
![Pasted_image_20250827222513.png](Imagenes/Pasted_image_20250827222513.png)
y encontramos la ruta
![Pasted_image_20250827222643.png](Imagenes/Pasted_image_20250827222643.png)
picamos en el archivo
![Pasted_image_20250827222710.png](Imagenes/Pasted_image_20250827222710.png)
copiamos y pegamos la clave secreta
![Pasted_image_20250827222742.png](Imagenes/Pasted_image_20250827222742.png)
