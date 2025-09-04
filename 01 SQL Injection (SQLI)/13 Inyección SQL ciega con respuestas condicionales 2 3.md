En esta clase continuamos con la explotación de la inyección SQL ciega introducida en la clase anterior. Nos centramos en determinar la longitud de la contraseña del usuario administrador, utilizando condiciones booleanas dentro del valor de la cookie y analizando si la respuesta incluye o no el mensaje “Welcome back”.

Este paso es clave antes de poder extraer el contenido completo del campo. Aprendes a automatizar la comprobación usando Burp Repeater.

Solucion 
esta captura lo que nos da es la primera letra de la contraseña del administrator con una ataque de fuerza bruta manual desde BS
![Pasted_image_20250702174001.png](Imagenes/Pasted_image_20250702174001.png)
Como lo hacemos con BS en ese campo le vamos add
![Pasted_image_20250702174222.png](Imagenes/Pasted_image_20250702174222.png)
luego nos vamos a paylod y desde la simple list agregamos desde la a-z y 0-9 y por ultimo quitamos el desmarcado que tenemos hasta abajo
![Pasted_image_20250702174455.png](Imagenes/Pasted_image_20250702174455.png)
Luego nos vamos a settings y nos vamos a grep Extract le damos al add agregamos el campo donde encontramos el error en este caso es welcome back le damos ok y por ultimo le damos start
![Pasted_image_20250702174825.png](Imagenes/Pasted_image_20250702174825.png)
y esto es para cada caracter pero lo que podemos hacer es saber cuantos caracteres tiene la contraseña en este caso tiene 20 con esta querry
![Pasted_image_20250702175230.png](Imagenes/Pasted_image_20250702175230.png)


