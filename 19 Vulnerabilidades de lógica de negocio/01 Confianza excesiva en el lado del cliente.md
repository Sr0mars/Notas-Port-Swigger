En esta clase vemos cómo un control excesivo en el cliente puede derivar en una lógica vulnerable. Durante el proceso de añadir un producto al carrito, observamos que el precio del artículo se incluye en el cuerpo de la petición.

Dado que el servidor no valida este dato, lo modificamos en Burp Repeater por un valor inferior al crédito disponible. Una vez ajustado, completamos la compra del artículo “Lightweight l33t leather jacket” por un precio mucho menor al real, resolviendo el laboratorio.

Solucion
La web:
![Pasted_image_20250827230635.png](Imagenes/Pasted_image_20250827230635.png)
nos logeamos y cuand nos logeamos nos da un credito de 100 pesos que pasa si tratamos de comprar algo mas caro
vamos a interceptar el add to cart
![Pasted_image_20250827230953.png](Imagenes/Pasted_image_20250827230953.png)
una ves interceptado vemos que tiene el precio vamos a tratar de cambiarlo
![Pasted_image_20250827231059.png](Imagenes/Pasted_image_20250827231059.png)
le vamos a poner 1000 (se traduce como 10$)y le damos forward
podemos ver que algo se me a agregado al carrito
![Pasted_image_20250827231215.png](Imagenes/Pasted_image_20250827231215.png)
y bueno le damos a placer order
![Pasted_image_20250827231326.png](Imagenes/Pasted_image_20250827231326.png)
y con esto se soluciona
![Pasted_image_20250827231400.png](Imagenes/Pasted_image_20250827231400.png)
