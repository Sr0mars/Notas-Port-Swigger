En esta clase vemos cómo una validación deficiente permite manipular la lógica del sistema. Tras añadir un producto barato al carrito, interceptamos la petición y cambiamos la cantidad a un valor negativo. Esto provoca que el sistema reste unidades y genere un total negativo.

Aprovechamos esta lógica para añadir la chaqueta “Lightweight l33t leather jacket” al carrito, y reducimos el precio total combinándolo con una cantidad negativa de otro artículo, logrando así completar la compra por debajo del crédito disponible y resolver el laboratorio.

Solucion
nos logeamos e interceptamos algun producto
![[Pasted image 20250827231804.png]]
podemos ver que ya no se emplea el precio por lo cual nosotros podemos poner un numero negativo
![[Pasted image 20250827232316.png]]
tal que vamos a interceptar un producto mas barato
![[Pasted image 20250827232403.png]]
![[Pasted image 20250827232444.png]]
tal que en el carrito se refleja una cantidad negativa
![[Pasted image 20250827232528.png]]
tal que si agregamos un producto que equilibre el precio a un numero positivo tendremos que pagar menos
![[Pasted image 20250827232651.png]]
asi que ahora vamos a probar con un producto mas caro
![[Pasted image 20250827232819.png]]
![[Pasted image 20250827233011.png]]
tal que al probar de nuevo obtenemos que si nos carga el producto caro a menor precio
![[Pasted image 20250827233042.png]]
