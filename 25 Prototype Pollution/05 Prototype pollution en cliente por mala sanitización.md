En esta clase nos enfrentamos a una aplicación que intenta bloquear ataques de prototype pollution usando una lista de claves prohibidas. Sin embargo, el filtro no se aplica de forma recursiva, lo que nos permite evadirlo utilizando claves alteradas como ‘**pro__proto__to**‘ que luego se normalizan a ‘**proto**‘ tras la deserialización.

Así logramos modificar ‘**Object.prototype**‘ y añadir propiedades arbitrarias. En el archivo ‘**searchLogger.js**‘ encontramos un gadget basado en ‘**transport_url**‘ que inserta dinámicamente una etiqueta script en el DOM si dicha propiedad existe. Aprovechamos esto inyectando un payload con una URL ‘**data:**‘ para ejecutar **alert(1)**.

Esta clase pone en evidencia cómo una sanitización incompleta o superficial puede ser fácilmente burlada, permitiendo llevar a cabo ataques de XSS del lado cliente.

Solucion
Entonces empezamos lo mismo ponemos la variable y vemos si tiene efecto
![Pasted image 20250831225646.png](imagenes/Pasted image 20250831225646.png)
vemos que no vemos nada asi que vamos al depurador para ver que hay
![Pasted image 20250831225800.png](imagenes/Pasted image 20250831225800.png)
y en la parte de abajo vemos una sanitizacion donde borra el proto
asi que  lo podemos burlar de esta forma
/?__pro__proto__to__[foo]=bar
![Pasted image 20250831230122.png](imagenes/Pasted image 20250831230122.png)
y vemos que ahi si se aplica por lo cual ahora si podemos efectuar la consulta
![Pasted image 20250831230250.png](imagenes/Pasted image 20250831230250.png)
