En esta clase analizamos cómo la caché interpreta y resuelve secuencias codificadas como ‘**..%2f**‘, mientras que el servidor no lo hace. Combinamos esta discrepancia con un delimitador URL como **%23**, que el servidor reconoce pero la caché no, para generar una ruta que la caché almacena con el contenido de **/my-account**.

Al forzar al usuario carlos a visitar dicha URL mediante un exploit en HTML, conseguimos que su respuesta se almacene y luego accedemos a ella directamente, extrayendo así su clave API.

Solucion
nos logeamos e interceptamos
![Pasted_image_20250902134535.png](/Imagenes/Pasted_image_20250902134535.png)
y aqui lo primero seria 
conocer el payload del intruder
![Pasted_image_20250902134631.png](/Imagenes/Pasted_image_20250902134631.png)
![Pasted_image_20250902134649.png](/Imagenes/Pasted_image_20250902134649.png)
asi que podemos probarlo en este caso lo mandamos en formato urlcode pero notenemos respuesta
![Pasted_image_20250902134757.png](/Imagenes/Pasted_image_20250902134757.png)
nos vamos al historico vemos que esta otra vez el historico pero este si contiene la cache
![Pasted_image_20250902135018.png](/Imagenes/Pasted_image_20250902135018.png)
entonces aqui es prueba y error podemos mezclar los #? para ver que nos sale o incluso urlcodearlos
vemos que aqui si sale
![Pasted_image_20250902135304.png](/Imagenes/Pasted_image_20250902135304.png)
asi que lo urlcodeamos el # 
![Pasted_image_20250902135408.png](/Imagenes/Pasted_image_20250902135408.png)
y quedaria algo asi en el exploit server se lo enviamos a la victima
![Pasted_image_20250902135610.png](/Imagenes/Pasted_image_20250902135610.png)nos vamos rapidamente al repeater send y nos llega la api key de carlos
![Pasted_image_20250902135655.png](/Imagenes/Pasted_image_20250902135655.png)
y ya solo copiamos y pegamos en la web
![Pasted_image_20250902135743.png](/Imagenes/Pasted_image_20250902135743.png)

