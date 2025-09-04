La aplicación permite cargar imágenes de productos a través de un parámetro ‘**filename**‘. Interceptamos esta petición y abusamos de la falta de validación para escalar directorios utilizando secuencias ‘**../**‘.

De esta forma, conseguimos acceder a archivos sensibles del sistema, como ‘**/etc/passwd**‘, demostrando una vulnerabilidad de path traversal en su forma más básica.

Solucion
La web:
![[Pasted image 20250814215729.png]]
vamos a copiar el link de la imagen y eso lo vamos a interceptar
![[Pasted image 20250814215809.png]]
una ves interceptado vamos a regresar unos directorios antes
../../../etc/passwd
![[Pasted image 20250814220250.png]]
y vemos la informacion
