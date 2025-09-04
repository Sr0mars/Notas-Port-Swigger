Aquí aplicamos un ataque de enumeración contra una base de datos MongoDB vulnerable. Primero identificamos la longitud de la contraseña usando condiciones como ‘**this.password.length < N**‘, y después iteramos sobre cada carácter usando Burp Intruder en modo Cluster bomb, combinando índices y letras.

De este modo, conseguimos descubrir la contraseña del administrador carácter a carácter, demostrando la potencia de la inyección NoSQL para extraer datos sensibles con precisión quirúrgica.

Solucion
entonces como nosotro ya dominamos el campo de user ahora lo que tocaria seria adivinar la longitud de la contraseña
se representaria asi
![Pasted_image_20250902010245.png](Imagenes/Pasted_image_20250902010245.png)
vamos a urlcodear los &&
tal que quedaria asi (administrator'%26%26this.password.length<9||')
![Pasted_image_20250902010521.png](Imagenes/Pasted_image_20250902010521.png)
y para saber el valor exacto quitamos el menor que y ponemos ==
vemos que el 8 es correcto
![Pasted_image_20250902010620.png](Imagenes/Pasted_image_20250902010620.png)
![Pasted_image_20250902010635.png](Imagenes/Pasted_image_20250902010635.png)tal que si queremos saber cual es la contraseña utilizaremos esto
![Pasted_image_20250902010833.png](Imagenes/Pasted_image_20250902010833.png)
el primer caracter es j![Pasted_image_20250902010936.png](Imagenes/Pasted_image_20250902010936.png)
pero para hacerlo mas facil lo vamos a mandar al intruder donde efectuaremos un ataque de tipo cluster bomb donde el primer payload sera numerico contando las 8 posiciones de la contraseña empezando desde el (0,1,2,3,4,5,6,7)
![Pasted_image_20250902011213.png](Imagenes/Pasted_image_20250902011213.png)
y el otro payload seria una listasimple desde la a-z
![Pasted_image_20250902011649.png](Imagenes/Pasted_image_20250902011649.png)
tal que una vez se complete nos dara la info en este caosi la contraseña es (jvtsgjvu)
![Pasted_image_20250902012649.png](Imagenes/Pasted_image_20250902012649.png)
![Pasted_image_20250902012801.png](Imagenes/Pasted_image_20250902012801.png)
