En este laboratorio se trabaja con una aplicación que utiliza objetos PHP serializados como mecanismo de sesión. Al iniciar sesión, se observa que la cookie contiene un objeto codificado en Base64 y URL.

Al decodificarlo, se descubre una estructura con un atributo **admin** configurado como falso (**b:0**). Al modificar este atributo a verdadero (**b:1**) y reenviar la petición, se otorgan privilegios administrativos al usuario.

Gracias a esto, se accede al panel de administración, desde donde es posible eliminar al usuario objetivo (carlos).

Esta técnica permite comprender cómo vulnerabilidades en la validación de objetos serializados pueden derivar en escaladas de privilegios severas si no se protegen adecuadamente.

Solucion
La web:
![Pasted_image_20250826203222.png](/Imagenes/Pasted_image_20250826203222.png)
nos logeamos
y una vez logeados lo interceptamos
![Pasted_image_20250826203326.png](/Imagenes/Pasted_image_20250826203326.png)
y bueno en la parte de la cookie si la seleccionamos podemos ver en la parte de abajo a la derecha me lo decodifoca dandonos datos
![Pasted_image_20250826203620.png](/Imagenes/Pasted_image_20250826203620.png)
tiene un valor 0 si lo cambiamos a 1 y aplicamos cambio y despues lo mandamos al repeater
![Pasted_image_20250826203733.png](/Imagenes/Pasted_image_20250826203733.png)
le damos send ya estando en el repeater y obtenemos una coockie de session
![Pasted_image_20250826203808.png](/Imagenes/Pasted_image_20250826203808.png)
por lo cual podemos irnos admin para modificar usuarios
![Pasted_image_20250826203941.png](/Imagenes/Pasted_image_20250826203941.png)
de tal manera que en el codigo fuente eliminamos el usuario carlos le damos send follow redirect 
![Pasted_image_20250826204108.png](/Imagenes/Pasted_image_20250826204108.png)
y ya solo recargamos pagina
![Pasted_image_20250826204137.png](/Imagenes/Pasted_image_20250826204137.png)
