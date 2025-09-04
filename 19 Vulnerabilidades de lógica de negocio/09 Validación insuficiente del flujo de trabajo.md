En esta clase aprovechamos un fallo lógico en la secuencia del proceso de compra. Tras adquirir un producto asequible con el crédito disponible, observamos que el servidor valida la compra únicamente al recibir una petición concreta de confirmación.

Más adelante, añadimos un artículo de mayor valor (la chaqueta) al carrito y simplemente repetimos la misma petición de confirmación usada anteriormente. El sistema no valida si el producto ha sido efectivamente pagado, ni si el crédito cubre el importe, permitiéndonos así adquirir la chaqueta sin coste y resolver el laboratorio.

Solucion
nos logeamos y agregamos una chaqueta al intentar comparla nos va salirun error el cual es obvio no tenemos el dinero
![[Pasted image 20250828225956.png]]
sin embargo nos vemos nada que podamos modificar el historico
![[Pasted image 20250828230303.png]]
asi que vamos a comprar algo mas barato
![[Pasted image 20250828230414.png]]
y vemos que se tramita un solicitud TRUE que basicamente valida la compra en el historico esto lo mandamos al repeater
![[Pasted image 20250828230509.png]]
y ahora agregamos la cachaqueta 
![[Pasted image 20250828230754.png]]
y tramitamos la solicitud que mandamos al repeater
![[Pasted image 20250828230843.png]]
y nos devuelve un 200 ok
por lo cual nosotros hemos resuelto el lab
![[Pasted image 20250828230919.png]]
