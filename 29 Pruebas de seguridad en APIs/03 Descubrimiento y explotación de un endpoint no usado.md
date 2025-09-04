En esta clase descubrimos un endpoint oculto gracias al uso del método **OPTIONS**, que revela que también es posible utilizar **PATCH**. Una vez autenticados, explotamos el endpoint enviando una petición con ‘**Content-Type: application/json**‘ y un cuerpo que modifica el precio del producto a cero.

Al actualizar la página, confirmamos el cambio de precio y completamos la compra del artículo para resolver el laboratorio.

Solucion
nos logeamos
![[Pasted image 20250902025129.png]]
y el objetivo es comprar la chaqueta asi que vamos a añadirla al carrito
![[Pasted image 20250902025230.png]]
pero no podemos comprar asi que vamos a pasar al historico
vemos una peticion products price lo mandamos al repeater
![[Pasted image 20250902025321.png]]bueno podemos emplear el metodo OPTIONS
![[Pasted image 20250902025503.png]]
lo ponemos aver que no sale
![[Pasted image 20250902025540.png]]
de primeras nos sale que el metodo no esta pero los que estan permitidos son GET y PATCH
Asi que si aplicamos el patch
![[Pasted image 20250902025739.png]]
nos sale el primero debemos de aplicar el json en la parte del response
asi que vamos añadir la cabecera content type y vamos a ver si podemos modificar el precio con el methodo patch
![[Pasted image 20250902030324.png]]
sin embargo si eliminamos la chaqueta y volvemos a recargar la pagina y no dirigimos nuevamente al producto podemos ver que cuesta 0
![[Pasted image 20250902030427.png]]
por lo cual lo agregamos y lo compramos
![[Pasted image 20250902030503.png]]
