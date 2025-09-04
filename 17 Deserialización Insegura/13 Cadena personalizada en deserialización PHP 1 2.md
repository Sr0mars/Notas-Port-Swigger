Accedemos al archivo ‘**CustomTemplate.php**‘ usando su versión de respaldo ‘**.php~**‘ y analizamos el flujo de ejecución del método mágico ‘**__wakeup()**‘.

Vemos cómo este método instancia un objeto ‘**Product**‘ usando dos atributos: ‘**default_desc_type**‘ y ‘**desc**‘. A su vez, ‘**desc**‘ puede contener un objeto **DefaultMap**, que implementa ‘**__get()**‘ con una llamada a ‘**call_user_func()**‘ que nos permite ejecutar funciones arbitrarias.

Combinando estos comportamientos, identificamos una cadena de gadgets que nos permite ejecutar comandos del sistema, como ‘**rm /home/carlos/morale.txt**‘, simplemente al deserializar un objeto bien construido.

Solucion
nos logeamos y mandamos al repeater
![Pasted image 20250827013850.png](imagenes/Pasted image 20250827013850.png)
asi que en esta parte probamos todo lo que aprendimos pero no funciona asi que pasamos a revisar la pagina para ver si encontramos algo
![Pasted image 20250827014040.png](imagenes/Pasted image 20250827014040.png)
encontramos este codigo, tuvimos que utilizar la tilde para poder ver el codigo
![Pasted image 20250827014237.png](imagenes/Pasted image 20250827014237.png)
Este sistema crea una plantilla de producto que puede tener una descripción en HTML o texto, y al serializar/deserializar el objeto, se conserva el tipo de descripción y se reconstruye el producto automáticamente. Es una forma elegante de mantener objetos ligeros y reactivarlos con lógica personalizada.

