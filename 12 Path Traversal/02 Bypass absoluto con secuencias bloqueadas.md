Aunque la aplicación filtra las secuencias clásicas de path traversal, como ‘**../**‘, permite especificar rutas absolutas desde el sistema de archivos raíz.

Al modificar el parámetro **filename** e indicar directamente ‘**/etc/passwd**‘, logramos leer el contenido del archivo sensible, demostrando que el filtrado es insuficiente y que no hay validación sobre rutas absolutas.

Solucion
![Pasted image 20250814221252.png](imagenes/Pasted image 20250814221252.png)
