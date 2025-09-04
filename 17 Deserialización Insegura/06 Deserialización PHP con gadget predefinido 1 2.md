En esta primera parte del laboratorio, analizamos el mecanismo de sesión basado en cookies firmadas con HMAC SHA-1. Al inspeccionar el contenido de la cookie, se identifica que contiene un objeto PHP serializado. Sin embargo, cualquier modificación invalida la firma, impidiendo su explotación directa.

Se encuentra un archivo de depuración expuesto (**/cgi-bin/phpinfo.php**) que revela que la aplicación usa Symfony 4.3.6. Además, en la salida del **phpinfo**, se expone la variable **SECRET_KEY**, que es fundamental para firmar de nuevo la cookie maliciosa con una firma válida.

Solucion
en este caso al igual que el otro nos apoyaremos de un repositorio de github (https://github.com/ambionics/phpggc)
![Pasted_image_20250826223932.png](/Imagenes/Pasted_image_20250826223932.png)
tenemos la web
![Pasted_image_20250826224025.png](/Imagenes/Pasted_image_20250826224025.png)
si nosotro checamos el codigo fuente podemos ver una ruta
![Pasted_image_20250826224057.png](/Imagenes/Pasted_image_20250826224057.png)
si lo copiamos y pegamos nos regresa un php info
![Pasted_image_20250826224212.png](/Imagenes/Pasted_image_20250826224212.png)
ahora vamos a interceptar despues del logearnos
![Pasted_image_20250826224754.png](/Imagenes/Pasted_image_20250826224754.png)
asi que vamos a llevarnos esa coockie a la terminal para decodificarla
![Pasted_image_20250826224951.png](/Imagenes/Pasted_image_20250826224951.png)
pero si vemos tambien tenemos una variable que se llama sig_hmac_sha1
![Pasted_image_20250826225138.png](/Imagenes/Pasted_image_20250826225138.png)
por lo cual no es modificable pero si buscamos en nuestro php info vemos que tenemos una secret key por lo cual nos puede ayudar a crear una key
![Pasted_image_20250826225409.png](/Imagenes/Pasted_image_20250826225409.png)
vamos a forzar un error eliminando unos caracteres de la cookie y nos sale
![Pasted_image_20250826225558.png](/Imagenes/Pasted_image_20250826225558.png)
![Pasted_image_20250826225628.png](/Imagenes/Pasted_image_20250826225628.png)
si vemos el git vemos que tiene symfony asi que vamos a compiarnos el git
![Pasted_image_20250826225729.png](/Imagenes/Pasted_image_20250826225729.png)
