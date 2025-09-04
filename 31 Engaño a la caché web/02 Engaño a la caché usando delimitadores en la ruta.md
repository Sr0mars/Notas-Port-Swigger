En esta clase identificamos caracteres especiales como ‘**;**’ que el servidor interpreta como delimitadores, pero que la caché ignora. Esto nos permite construir una URL que, al contener una extensión como ‘**.js**‘, es almacenada por la caché. Luego, forzamos a la víctima (carlos) a visitar esa URL con su sesión iniciada, haciendo que se cachee su clave API.

Finalmente, accedemos a la misma ruta y obtenemos su clave desde la respuesta almacenada.

Solucion
El servidor lo puede interpretar asi
![Pasted_image_20250902131417.png](/Imagenes/Pasted_image_20250902131417.png)
tenemos un diccionario que nos puede servir mas adelante para BF
![Pasted_image_20250902131605.png](/Imagenes/Pasted_image_20250902131605.png)
asi que lo primero seria logearnos
![Pasted_image_20250902131653.png](/Imagenes/Pasted_image_20250902131653.png)
vamos a interceptarlo y lo mandamos al repeater
![Pasted_image_20250902131816.png](/Imagenes/Pasted_image_20250902131816.png)
podemos probar lo del otro laboratorio pero no va funcionar asi que algo que podemos hacer es esto
![Pasted_image_20250902131904.png](/Imagenes/Pasted_image_20250902131904.png)
y vamos a mandarlo al intruder seleccionamos como payload el ? y vamos a emplear la lista
![Pasted_image_20250902132151.png](/Imagenes/Pasted_image_20250902132151.png)
y podemos ver que el ; tambien se emplea
![Pasted_image_20250902132321.png](/Imagenes/Pasted_image_20250902132321.png)
y si ahora lo probamos
![Pasted_image_20250902132412.png](/Imagenes/Pasted_image_20250902132412.png)
vemos que la cache se reinicia
asi que podemos hacer lo mismo en el exploit server
![Pasted_image_20250902132552.png](/Imagenes/Pasted_image_20250902132552.png)
y ahora visitamos la web y otorgamos la api key
![Pasted_image_20250902132640.png](/Imagenes/Pasted_image_20250902132640.png)
