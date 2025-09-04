En esta clase analizamos cómo, al repetir suficientes veces una petición que añade unidades al carrito, conseguimos que el total supere el valor máximo permitido por el tipo de dato entero usado por el backend (2,147,483,647). Esto provoca un overflow que hace que el precio total pase a ser negativo.

Este comportamiento inesperado sienta las bases para forzar el valor del carrito a una cifra dentro de nuestro crédito disponible.

Solucion
nos logeamos y inteceptamos la chaqueta y en este caso no se pueden poner numeros negativos sin embargo me permite poner una cantidad de hasta 99 que seria el tope esto lo vamos a mandar al intruder
![Pasted image 20250828212046.png](imagenes/Pasted image 20250828212046.png)
ya estando en el intruder no vamos agregar nada solamente vamos a modificar la seccion de payloads
![Pasted image 20250828212351.png](imagenes/Pasted image 20250828212351.png)
y en resource pool
![Pasted image 20250828212440.png](imagenes/Pasted image 20250828212440.png)
le damos start attack
![Pasted image 20250828212544.png](imagenes/Pasted image 20250828212544.png)
tal que como vallamos refrescando la pagina va aumentando
![Pasted image 20250828212619.png](imagenes/Pasted image 20250828212619.png)
![Pasted image 20250828212710.png](imagenes/Pasted image 20250828212710.png)
y bueno despues de varias refresh vemos que el precio se ah quedado en un valor negativo
![Pasted image 20250828213455.png](imagenes/Pasted image 20250828213455.png)
Esto por que se da
![Pasted image 20250828213332.png](imagenes/Pasted image 20250828213332.png)

