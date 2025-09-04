En esta clase aprovechamos un fallo lógico en la validación de cupones dentro del proceso de compra. Aunque el sistema impide aplicar el mismo cupón más de una vez consecutiva, permite alternar entre distintos cupones sin comprobar si ya fueron usados.

Al alternar repetidamente los códigos **NEWCUST5** y **SIGNUP30**, logramos aplicar múltiples descuentos acumulativos. Así conseguimos bajar el precio de la chaqueta por debajo de nuestro crédito y completar la compra con éxito, resolviendo el laboratorio.

Solucion
y bueno al acceder a la web nos sale que tenemos un codigo de descuento
![Pasted image 20250827234513.png](imagenes/Pasted image 20250827234513.png)
mos logeamos y en la parte de hasta abajo de la web nos sale esto
![Pasted image 20250827234638.png](imagenes/Pasted image 20250827234638.png)
vamos a tratar de validar y nos sale otro codigo
![Pasted image 20250827234722.png](imagenes/Pasted image 20250827234722.png)
bueno vamos a agregar la chaqueta y aplicamos los codigo de descuento
![Pasted image 20250827234942.png](imagenes/Pasted image 20250827234942.png)
pero que pasa si vamos alternando los codigos
![Pasted image 20250827235116.png](imagenes/Pasted image 20250827235116.png)
de tal manera que el precio se queda en 0
![Pasted image 20250827235140.png](imagenes/Pasted image 20250827235140.png)
