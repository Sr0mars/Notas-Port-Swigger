Aquí automatizamos la compra y canje de tarjetas regalo configurando una macro personalizada en Burp Suite. Usamos Burp Intruder para lanzar cientos de peticiones secuenciales que ejecutan este flujo con la ayuda de una sesión manipulada, generando así saldo suficiente para comprar el artículo objetivo (la chaqueta) y resolver el laboratorio.

Solucion
3.- seria el check out
![[Pasted image 20250828234406.png]]
4.- tambien la de la confirmacion de la orden
![[Pasted image 20250828234743.png]]
5.- y la ultima donde se envia el codigo
![[Pasted image 20250828234855.png]]
le damos ok
y vamos a configurar esta peticion en configure item
![[Pasted image 20250828235158.png]]
y bueno aqui le vamos a dar add
![[Pasted image 20250828235312.png]]
y en este punto vamos a poner el nombre de la siguiente solicitud y vamos a seleccionar el codigo de descuento y le damos ok
![[Pasted image 20250828235506.png]]
tal que quedaria asi le damos ok
![[Pasted image 20250828235541.png]]
y ahora configuramos la siguiente que seria la de gift card tal que se vea asi
![[Pasted image 20250828235652.png]]
le damos a test macro
![[Pasted image 20250828235749.png]]
y una forma de comprobarlo seria recargado de nuevo la pagina
tal que ahora 
se aumento el dinero
![[Pasted image 20250828235851.png]]
y le damos ok a las ventanas menos a la penultima y en el scope lo midificamos para todas la url
![[Pasted image 20250829000027.png]]
y ahora lo cerramos todo
![[Pasted image 20250829000115.png]]
de esta manera ya queda automatizado 
y ya solo mandamos un peticion por ejemplo la de la raiz al repeater y le damos a send podemos ver que se va incrementando
![[Pasted image 20250829000348.png]]
tal que quedaria asi
![[Pasted image 20250829000545.png]]
y en el resource poll lo modificamos
![[Pasted image 20250829000808.png]]
y se automatiza por lo cual ya es cuestion de esperarnos
![[Pasted image 20250829000922.png]]
una vez termina ya 
podemos ver el resultado
![[Pasted image 20250829005751.png]]
asi que ahora si podemos comprar la chaqueta
![[Pasted image 20250829005847.png]]

