En este laboratorio, la aplicación gestiona sesiones a través de objetos PHP serializados que incluyen atributos como la ruta al avatar del usuario.

Mediante la función legítima de eliminar cuenta, se puede explotar un comportamiento peligroso del servidor: al eliminar al usuario, el sistema también elimina el archivo indicado por el atributo ‘**avatar_link**‘.

Al modificar dicho atributo para que apunte al archivo ‘**/home/carlos/morale.txt**‘, la aplicación termina borrando ese fichero en lugar del avatar.

Esto demuestra cómo una funcionalidad inofensiva, combinada con una deserialización insegura, puede escalar a una explotación crítica mediante la manipulación de datos serializados.

Solucion
de igual nos logeamos y lo interceptamos
![Pasted_image_20250826210609.png](/Imagenes/Pasted_image_20250826210609.png)
una vez en el repeater vemos la coockie y notamos que tienen otro campo el cual se llama avatar_link el cual tiene como funcion eliminar el usuario pero si en vez de eso eliminamos el archivo que nos pide el laboratorio poniendo la direccion en donde se encuentra
![Pasted_image_20250826210730.png](/Imagenes/Pasted_image_20250826210730.png)
tal que quedaria asi nos copiamos la cookie de session la pegamos en el navegador
![Pasted_image_20250826210945.png](/Imagenes/Pasted_image_20250826210945.png)
ahora que tenemos la cookie pegada en el navegador pasamos a presionar el boton de delet account el cual conllevara a eliminar el archivo que hemos puesto
de tal manera que se solucionara el laboratorio
![Pasted_image_20250826211629.png](/Imagenes/Pasted_image_20250826211629.png)

