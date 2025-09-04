En esta clase comenzamos explorando cómo las aplicaciones que construyen internamente peticiones a APIs pueden ser vulnerables a Server-Side Parameter Pollution. Analizamos cómo añadir parámetros adicionales codificados con **%26** (carácter **&**) puede ser interpretado como una inyección de parámetros por el servidor.

Este comportamiento se identifica gracias a los mensajes de error que van revelando qué parámetros internos existen, permitiéndonos deducir la estructura del backend.

Solucion
![Pasted_image_20250902022319.png](/Imagenes/Pasted_image_20250902022319.png)
no nos dan credencial de momento vamos a probar otra cosa como forgot
![Pasted_image_20250902022551.png](/Imagenes/Pasted_image_20250902022551.png)
vamos a probar con administrator
![Pasted_image_20250902022620.png](/Imagenes/Pasted_image_20250902022620.png)
nos sale esto 
![Pasted_image_20250902022634.png](/Imagenes/Pasted_image_20250902022634.png)
vamos a ver el historico notamos una seccion de forgot password donde tiene contenido lo mandamos al repeater
![Pasted_image_20250902022747.png](/Imagenes/Pasted_image_20250902022747.png)
tambien vemos una peticion post al forgot
![Pasted_image_20250902022922.png](/Imagenes/Pasted_image_20250902022922.png)
tambien la mandamos al repeater
y algo que podemos hacer es ponerle un parametro # que se representa en urlcode como %23
![Pasted_image_20250902023210.png](/Imagenes/Pasted_image_20250902023210.png)
y vamos a aprovecharnos de este error poniendolo asi
![Pasted_image_20250902023404.png](/Imagenes/Pasted_image_20250902023404.png)
entonces algo que podemos hacer es aplicar fuerza bruba al campo de test para descubrir campos potencialmente validos (recordemos que el %26 es el &) asi que ahora vamos a modificar test por x para asi hacerlo mas facil en el intruder
y vamos a emplear esta lista ([burp-payloads/Server-side variable names.pay at master · antichown/burp-payloads · GitHub](https://github.com/antichown/burp-payloads/blob/master/Server-side%20variable%20names.pay))
![Pasted_image_20250902024217.png](/Imagenes/Pasted_image_20250902024217.png)
y nos arroja estos resultados
![Pasted_image_20250902024238.png](/Imagenes/Pasted_image_20250902024238.png)
los podemos probar en el repeater
![Pasted_image_20250902024319.png](/Imagenes/Pasted_image_20250902024319.png)
![Pasted_image_20250902024337.png](/Imagenes/Pasted_image_20250902024337.png)
y si nos vamos a la otra tab podemos ver que se emplea una variable reset_token que basicamente
![Pasted_image_20250902024514.png](/Imagenes/Pasted_image_20250902024514.png)
![Pasted_image_20250902024627.png](/Imagenes/Pasted_image_20250902024627.png)
lo probamos
![Pasted_image_20250902024721.png](/Imagenes/Pasted_image_20250902024721.png)
asi que este token lo ponemos en la url
![Pasted_image_20250902024825.png](/Imagenes/Pasted_image_20250902024825.png)
le damos enter ahora podemos cambiar la contraseña de administrador
![Pasted_image_20250902024858.png](/Imagenes/Pasted_image_20250902024858.png)
nos logeamos como administrador y eliminamos al usuario carlos
![Pasted_image_20250902024944.png](/Imagenes/Pasted_image_20250902024944.png)



