El recurso ‘**/js/localize.js**‘ también es vulnerable a inyección de cabeceras si se le pasa ‘**cors=1**‘ en la URL y se añade una cabecera Origin maliciosa. Si se logra insertar saltos de línea dentro del valor de **Origin**, es posible inyectar cabeceras HTTP completas, incluyendo una carga útil como ‘**alert(1)**‘.

Este tipo de ataque permite alterar el cuerpo de la respuesta y convertir el archivo ‘**localize.js**‘ en un vector de XSS, siempre que se consiga cachear esa versión manipulada.

Solucion
tal que el x-cache key lo necesitamos poner pero en la parte del login donde va la ruta asi que hay que URL-codearlo por que si no da problema
 ![Pasted image 20250822202413.png](imagenes/Pasted image 20250822202413.png)
 y cuando le damos send podemos ver en el login en el codigo fuente de la pagina que ya se nos aplica el src
 ![Pasted image 20250822202605.png](imagenes/Pasted image 20250822202605.png)
 