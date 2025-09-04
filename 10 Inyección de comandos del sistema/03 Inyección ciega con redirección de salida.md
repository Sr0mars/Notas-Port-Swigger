En esta clase resolvemos una inyección de comandos del sistema operativo en modo ciego, utilizando redirección de salida para obtener los resultados. Aprovechamos que el directorio ‘**/var/www/images/**‘ es escribible, inyectando el comando ‘**whoami**‘ y redirigiendo su salida a un archivo dentro de esa carpeta (**output.txt**).

Luego accedemos a ese archivo a través del sistema de carga de imágenes, logrando visualizar el resultado del comando ejecutado en el servidor.

Solucion
Al igual que el anterior laboratorio el campo vulnerable vuelve a hacer email
![Pasted_image_20250813232245.png](/Imagenes/Pasted_image_20250813232245.png)
injectamos el comando y ahora quedaria ir a buscar el archivo le picamos en caulquier imagen par aver la ruta
![Pasted_image_20250813232332.png](/Imagenes/Pasted_image_20250813232332.png)
y solamente ponemos la direccion
![Pasted_image_20250813232506.png](/Imagenes/Pasted_image_20250813232506.png)

