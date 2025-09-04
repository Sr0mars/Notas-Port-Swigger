En esta clase replicamos la explotación de una condición de carrera usando únicamente la edición gratuita de Burp Suite. Agrupamos varias pestañas en Repeater con la misma solicitud de aplicación de descuento, y tras enviarlas en paralelo, observamos que más de una es aceptada, a pesar de que solo debería permitirse una.

Esta técnica demuestra que el sistema aplica los descuentos de forma concurrente y no bloquea correctamente los intentos repetidos si se envían al mismo tiempo. Aprovechamos esto para reducir el precio del artículo objetivo —una chaqueta de cuero— y finalizar la compra por debajo del crédito disponible.

Esta clase muestra cómo es posible explotar condiciones de carrera incluso sin herramientas profesionales.

Solucion
entonces que pasa aqui vamos agregar la chaqueta
![[Pasted image 20250901181611.png]]
ahora vamos a interceptar la parte del cupon por BS y lo mandams al repeater
![[Pasted image 20250901181722.png]]
y creamos un grupo
![[Pasted image 20250901181923.png]]
le vamos a poner click derecho y lo vamos a duplicar unas 30 veces
![[Pasted image 20250901182002.png]]
![[Pasted image 20250901182029.png]]
y lo vamos a mandar asi
![[Pasted image 20250901182107.png]]
y vemos que no ha mandado muchas
![[Pasted image 20250901182256.png]]
vamos a crear otras 20
y bueno el chiste es estar removiendo la promo y mandandola de nuevo por bs hasta que se haga un descuento mas o menos
![[Pasted image 20250901182446.png]]
de tal manera que aqui si nos alcanza por lo que compramos y resolvemos el lab
![[Pasted image 20250901182526.png]]

