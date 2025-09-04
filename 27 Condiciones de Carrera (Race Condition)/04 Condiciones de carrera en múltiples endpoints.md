En esta clase analizamos cómo distintas rutas del flujo de compra pueden ser utilizadas de forma simultánea para provocar inconsistencias en la lógica del servidor. En concreto, usamos los endpoints de añadir productos al carrito y realizar el pago en paralelo, intentando insertar productos costosos en el momento justo en que el servidor valida el crédito del usuario pero antes de que lo consuma.

A través de este desfase entre validación y confirmación, logramos adquirir un artículo caro como la chaqueta ‘**L33t**‘ por un precio inferior al real.

El laboratorio demuestra cómo incluso una buena validación puede romperse cuando diferentes procesos no están bien sincronizados.

Solucion
para empezar lo primero que vamos hacer es logearnos
e vamos a interceptar algun añadir producto y lo mandamos al repeater
![Pasted image 20250901191635.png](imagenes/Pasted image 20250901191635.png)
luego interceptamos la compra y de igual forma lo mandamos al repeater
![Pasted image 20250901191907.png](imagenes/Pasted image 20250901191907.png)
y ahora con estas 2 tab vamos a crear un grupo con el objetivo de medir los tiempos en los cuales se envian las solicitudes
![Pasted image 20250901192313.png](imagenes/Pasted image 20250901192313.png)
y si miramos en la parte de abajo en la derecha podemos ver la velocidad en la que se manda aqui la de cart
![Pasted image 20250901192355.png](imagenes/Pasted image 20250901192355.png)
y esta la de checkout
![Pasted image 20250901192417.png](imagenes/Pasted image 20250901192417.png)
y esto puede suponer un problema
por que si nosotros cambiamos el id por el de la chaqueta y cambiamos grupo por paralelo
![Pasted image 20250901193558.png](imagenes/Pasted image 20250901193558.png)
y le damos a send
y lo verificamos en la otra pestaña
![Pasted image 20250901193705.png](imagenes/Pasted image 20250901193705.png)
se no ah agregado la chaqueta la gift card
