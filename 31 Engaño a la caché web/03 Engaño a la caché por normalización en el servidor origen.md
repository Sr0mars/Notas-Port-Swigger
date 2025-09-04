En esta clase exploramos cómo el servidor de origen interpreta rutas con secuencias de directorios codificadas como ‘**..%2f**‘, mientras que la caché no las resuelve. Aprovechamos esto junto con un prefijo de ruta estática (resources) que activa reglas de caché. Al construir una ruta como ‘**/resources/..%2fmy-account**‘, conseguimos cachear la clave API del usuario carlos tras redirigirlo con un exploit.

Finalmente, accedemos a esa misma ruta y extraemos su clave desde la caché.

Solucion
nos logeamos y lo interceptamos
![Pasted_image_20250902132902.png](Imagenes/Pasted_image_20250902132902.png)
![Pasted_image_20250902133006.png](Imagenes/Pasted_image_20250902133006.png)
asi que vamos aplicar BF
nos sale en esta ocacion el payload es el ?
![Pasted_image_20250902133031.png](Imagenes/Pasted_image_20250902133031.png)
sin embargo cuando lo probamos no nos sale nada de la cache
![Pasted_image_20250902133118.png](Imagenes/Pasted_image_20250902133118.png)
algo que podemos hacer es irnos al historico y ver si alguna emplea cache y vemos una donde se emplea el src
![Pasted_image_20250902133416.png](Imagenes/Pasted_image_20250902133416.png)
asi que aqui si se emplea la cache
![Pasted_image_20250902133527.png](Imagenes/Pasted_image_20250902133527.png)
algo que podemos hacer es regresarnos al tab1 y retroceder algunos directorios y poner la direccion de resources
vemos que si funciona
![Pasted_image_20250902133641.png](Imagenes/Pasted_image_20250902133641.png)
entonces algo que podemos hacer es urlcodear el / que seria %2f
![Pasted_image_20250902134111.png](Imagenes/Pasted_image_20250902134111.png)
y esto lo aplicamos en el exploit server
![Pasted_image_20250902134133.png](Imagenes/Pasted_image_20250902134133.png)
y le la damos a deliver y rapidamente nos vamos a al repeater y le damos send
![Pasted_image_20250902134213.png](Imagenes/Pasted_image_20250902134213.png)
vemos que la cache es 4 y no 0
por lo cual ya podemos ver la api key de carlos
![Pasted_image_20250902134243.png](Imagenes/Pasted_image_20250902134243.png)
y ya solo lo ponemos en la web
![Pasted_image_20250902134321.png](Imagenes/Pasted_image_20250902134321.png)
