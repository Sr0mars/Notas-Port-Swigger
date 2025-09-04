En esta clase nos enfrentamos a una funcionalidad de subida de archivos que bloquea directamente ciertas extensiones, como .php, mediante una lista negra. Sin embargo, esta defensa resulta ineficaz debido a una mala configuración en el servidor Apache, que nos permite modificar el comportamiento del servidor usando un archivo .htaccess.

Subimos un **.htaccess** que redefine una extensión arbitraria, como ‘**.s4vitar**‘, para que sea tratada como código PHP. Luego subimos nuestra shell PHP renombrada con esta nueva extensión y conseguimos que el servidor la ejecute igualmente. Esta técnica ilustra cómo los mecanismos de seguridad mal planteados pueden ser fácilmente burlados mediante configuraciones del servidor accesibles al atacante.

Solucion
asi que nos logeamos subimos la shell pero nos sale esto
![Pasted image 20250830203741.png](imagenes/Pasted image 20250830203741.png)
le damos click y nos vamos al historico y la peticion post la mandamos al repeater
![Pasted image 20250830203840.png](imagenes/Pasted image 20250830203840.png)
y probando lo de los demas laboratorios vemos que no se podra pero lo que podemos hacer es subir un archivo .htaccess
![Pasted image 20250830204105.png](imagenes/Pasted image 20250830204105.png)
y nosotros podemos agregar esto
(AddType application/x-httpd-php .omar)
tal que quedaria asi vemos en esta parte que si nos permite subir este tipo de archivos
![Pasted image 20250830204429.png](imagenes/Pasted image 20250830204429.png)
ahora retrocedemos y lo probamos cambiandole la extencion a .omar
![Pasted image 20250830204530.png](imagenes/Pasted image 20250830204530.png)
y lo a subido
asi que nos vamos en la web y lo probamos para ver si se subio el archivo
![Pasted image 20250830204713.png](imagenes/Pasted image 20250830204713.png)
y ya solo copiamos y pegamos
![Pasted image 20250830204744.png](imagenes/Pasted image 20250830204744.png)


