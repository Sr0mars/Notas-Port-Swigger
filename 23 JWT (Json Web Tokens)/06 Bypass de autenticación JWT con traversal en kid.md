En esta clase nos enfrentamos a una implementación insegura de JWT donde el servidor utiliza el valor del parámetro kid para leer desde el sistema de archivos la clave con la que validar la firma del token. Aprovechamos esto introduciendo una secuencia de path traversal en **kid** que apunta al archivo **/dev/null**, el cual tiene contenido predecible.

Firmamos nuestro JWT con una clave basada en un byte nulo y modificamos el payload para suplantar al usuario administrador. El servidor usa **/dev/null** como clave de verificación sin realizar validaciones adecuadas, por lo que acepta el token y nos concede acceso al panel de administración, desde donde eliminamos a Carlos.

Este laboratorio demuestra cómo una gestión insegura del parámetro **kid** puede comprometer completamente el control de autenticación.

Solucion
nos logeamos y aqui lo interceptamos
![Pasted_image_20250831011358.png](/Imagenes/Pasted_image_20250831011358.png)
podemos ver que estamos ante una clave simetrica
![Pasted_image_20250831011425.png](/Imagenes/Pasted_image_20250831011425.png)
nos vamos a la extencion del JWT y vamos acrear una key symetrica
![Pasted_image_20250831011759.png](/Imagenes/Pasted_image_20250831011759.png)
y en la parte de la k vamos a poner un valor nulo
![Pasted_image_20250831011826.png](/Imagenes/Pasted_image_20250831011826.png)
![Pasted_image_20250831011918.png](/Imagenes/Pasted_image_20250831011918.png)
le damos a ok
y en la cabecera le vamos a quitar el kid y vamos a retroceder unos directores hasta y ponemos el dev null
![Pasted_image_20250831012149.png](/Imagenes/Pasted_image_20250831012149.png)
seguido le damos a sign
![Pasted_image_20250831012228.png](/Imagenes/Pasted_image_20250831012228.png)
copiamos la cookie y eliminamos al usuario carlos
![Pasted_image_20250831012423.png](/Imagenes/Pasted_image_20250831012423.png)
