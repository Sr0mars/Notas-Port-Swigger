En esta clase descubrimos cómo generar crédito en la cuenta explotando una lógica defectuosa: al comprar tarjetas regalo con descuento mediante un cupón (**SIGNUP30**), y luego canjearlas, el crédito obtenido es mayor al dinero gastado. Esto permite repetir el proceso indefinidamente y acumular saldo en la cuenta.

Solucion
nos logeamos pero vemos un apartado de gift cards
![Pasted_image_20250828232623.png](Imagenes/Pasted_image_20250828232623.png)
y explorando la pagina vemos que tenemos un apartado de codigos
![Pasted_image_20250828232715.png](Imagenes/Pasted_image_20250828232715.png)
nos dan un codigo
![Pasted_image_20250828232735.png](Imagenes/Pasted_image_20250828232735.png)
si nosotros agregamos una gift card al carrito
![Pasted_image_20250828233134.png](Imagenes/Pasted_image_20250828233134.png)
y aplicamos el codigo de descuento
![Pasted_image_20250828233206.png](Imagenes/Pasted_image_20250828233206.png)
lo compramos
![Pasted_image_20250828233236.png](Imagenes/Pasted_image_20250828233236.png)
ahora ese codigo lo canjeamos
![Pasted_image_20250828233312.png](Imagenes/Pasted_image_20250828233312.png)
por lo cual va aumentando nuestro dinero una vez que lo aplicamos
![Pasted_image_20250828233354.png](Imagenes/Pasted_image_20250828233354.png)
por lo cual vamos a crear una macro (en add le ponemos add a macro)
![Pasted_image_20250828233838.png](Imagenes/Pasted_image_20250828233838.png)
para la macro 
1.- el producto que añade al carrito
![Pasted_image_20250828234017.png](Imagenes/Pasted_image_20250828234017.png)
2.- la siguiente seria la que aplicamos el cupon SIGNUP30
![Pasted_image_20250828234140.png](Imagenes/Pasted_image_20250828234140.png)

