En esta clase nos encontramos con una interfaz de administración protegida por autenticación. Al enviar una petición usando el método **HTTP TRACE**, descubrimos que el servidor refleja una cabecera personalizada (**X-Custom-IP-Authorization**) con nuestra IP.

Este comportamiento revela una cabecera utilizada internamente para validar si una solicitud proviene de localhost. Al añadir manualmente esta cabecera con el valor **127.0.0.1**, conseguimos acceder al panel de administración y eliminar al usuario carlos, resolviendo el laboratorio.

Solucion
nos logeamos y si revisamos en el http history
![Pasted_image_20250827223213.png](/Imagenes/Pasted_image_20250827223213.png)
no vemos nada vamos a poner la ruta /admin para ver que nos arroja y eso lo mandamos al repeater
![Pasted_image_20250827223314.png](/Imagenes/Pasted_image_20250827223314.png)
de primeras no vemos nada
![Pasted_image_20250827223511.png](/Imagenes/Pasted_image_20250827223511.png)
pero es posible poner el metodo trace
![Pasted_image_20250827223552.png](/Imagenes/Pasted_image_20250827223552.png)
![Pasted_image_20250827223712.png](/Imagenes/Pasted_image_20250827223712.png)
y vemos esta cabecera asi que nosotros podemos poner esta cabecera y mandarlo al localhost
tal que si nosotro ponemos esto en el metodo get podemos ver el panel del admin
![Pasted_image_20250827223908.png](/Imagenes/Pasted_image_20250827223908.png)
y con esto podemos eliminar al usuario
![Pasted_image_20250827223954.png](/Imagenes/Pasted_image_20250827223954.png)
