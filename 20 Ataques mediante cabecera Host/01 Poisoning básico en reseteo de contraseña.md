En esta clase exploramos una vulnerabilidad de tipo password reset poisoning, aprovechando una falta de validación en la cabecera Host del servidor. Al iniciar el proceso de recuperación de contraseña, se genera un enlace con un token temporal que es enviado por correo. Sin embargo, si manipulamos la cabecera **Host** en la petición de reseteo, el servidor incluirá esa cabecera manipulada en el enlace enviado al usuario.

Carlos, un usuario descuidado, accederá al enlace con ese dominio malicioso, haciendo que su navegador nos envíe la solicitud con el token de reseteo a nuestro servidor. Desde los registros de acceso, capturamos el token, lo utilizamos para modificar su contraseña y accedemos a su cuenta. Se explica paso a paso cómo identificar esta lógica vulnerable, manipular el Host, interceptar el token y completar el acceso no autorizado.

Solucion
La web:
![Pasted_image_20250829195610.png](Imagenes/Pasted_image_20250829195610.png)
en el apartado de login tenemos un apartado de password de igual manera nos comparten un exploit server
![Pasted_image_20250829195654.png](Imagenes/Pasted_image_20250829195654.png)
le damos forgot password
![Pasted_image_20250829195839.png](Imagenes/Pasted_image_20250829195839.png)
ponemos el usuario de wiener y nos mandara una nota que se mandara al correo
![Pasted_image_20250829195950.png](Imagenes/Pasted_image_20250829195950.png)
lo checamos en el exploit server
![Pasted_image_20250829200017.png](Imagenes/Pasted_image_20250829200017.png)
![Pasted_image_20250829200100.png](Imagenes/Pasted_image_20250829200100.png)
y se le damos podemos notar que en la url hay una validacion de token
![Pasted_image_20250829200214.png](Imagenes/Pasted_image_20250829200214.png)
asi que si vemos en el historico la peticion de forgot password esto lo vamos a mandar al repeater para ver si podemos poner un token valido
![Pasted_image_20250829200317.png](Imagenes/Pasted_image_20250829200317.png)
que podemos hacer aqui pues claramanete modificar la cabecera host que tenemos y en vez de poner la url de la pagina ponemos la de nuestro exploit server del tal manera que quedaria asi
![Pasted_image_20250829200854.png](Imagenes/Pasted_image_20250829200854.png)
asi que le damos a send y en el exploit server vemos los logs
![Pasted_image_20250829201058.png](Imagenes/Pasted_image_20250829201058.png)
copiamos esto y lo pegamos en la url donde se cambia la contraseña
![Pasted_image_20250829201153.png](Imagenes/Pasted_image_20250829201153.png)
de tal manera que la podemos cambiar
![Pasted_image_20250829201218.png](Imagenes/Pasted_image_20250829201218.png)
probamos
![Pasted_image_20250829201246.png](Imagenes/Pasted_image_20250829201246.png)
y hemos logrado cambiar la contraseña de carlos
![Pasted_image_20250829201308.png](Imagenes/Pasted_image_20250829201308.png)

