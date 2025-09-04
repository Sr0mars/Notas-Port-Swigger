En esta clase aprenderás a explotar una vulnerabilidad basada en el tiempo de respuesta del servidor para identificar nombres de usuario válidos. A través de Burp Suite, lanzarás un ataque tipo timing aprovechando que el servidor tarda más en responder cuando el nombre de usuario es correcto pero la contraseña es incorrecta y larga.

Además, el laboratorio implementa un sistema de bloqueo por IP tras varios intentos fallidos, lo cual se evita manipulando la cabecera ‘**X-Forwarded-For**‘ para simular distintas direcciones IP. Una vez identificado un usuario válido, realizarás un ataque por diccionario contra su contraseña hasta obtener acceso a su cuenta.

Solucion
y bueno en esta ocacion podemos ver que cuando nosotros intentamos muchas veces intertar logearnos nos manda un error de que hay que esperar este es el caso en este laboratorio
asi que esto lo vamos a interceptar y mandar al repeter
![Pasted_image_20250819200056.png](Imagenes/Pasted_image_20250819200056.png)
pero exite una cabecera que puede hacer que se reinice la cuenta basicamente engaña a la web haciendo parecer que se conecta a otro servidor (**X-Forwarded-For: 127.0.0.2**)
![Pasted_image_20250819200252.png](Imagenes/Pasted_image_20250819200252.png)
asi que ahora tenemos 3 intentos mas
![Pasted_image_20250819200339.png](Imagenes/Pasted_image_20250819200339.png)
ahora otra cosa que nosotros podemos probar es que si ala hora de poner muchas caracteres en la contraseña el servidor tardara en contestar
![Pasted_image_20250819200501.png](Imagenes/Pasted_image_20250819200501.png)
esto solo se aplica si el usuario es correcto por lo cual tarda en dar la respuesta asi que esto lo podemos mandar al intruder
asi que en este ataque vamos a implementar el pitchfork (lo que hace es que se efectuen varios ataques)
![Pasted_image_20250819200627.png](Imagenes/Pasted_image_20250819200627.png)
entonces configuramos el primer payload que es el del usuario quitando el urlcode
![Pasted_image_20250819200920.png](Imagenes/Pasted_image_20250819200920.png)
y el segundo payload va ser de tipo numerico con una secuencia del 1 al 100
![Pasted_image_20250819201134.png](Imagenes/Pasted_image_20250819201134.png)
pero lo hemos echo al reves en el segundo va el ataque de usuarios
![Pasted_image_20250819201434.png](Imagenes/Pasted_image_20250819201434.png)
![Pasted_image_20250819201449.png](Imagenes/Pasted_image_20250819201449.png)
y ahora asi le damos startatack

y bueno aqui podemos ver que el usuario user tiene un numero bastante grande por lo cual la unica forma de comprobar si es un usuario valido es mandandolo al repeter
![Pasted_image_20250819202107.png](Imagenes/Pasted_image_20250819202107.png)
le damos send y vemos que igual se tarda
![Pasted_image_20250819202145.png](Imagenes/Pasted_image_20250819202145.png)asi que ahora volvemos a repetir el proceso pero en esta ocacion para la contraseña
![Pasted_image_20250819202405.png](Imagenes/Pasted_image_20250819202405.png)
![Pasted_image_20250819202818.png](Imagenes/Pasted_image_20250819202818.png)
![Pasted_image_20250819203237.png](Imagenes/Pasted_image_20250819203237.png)
