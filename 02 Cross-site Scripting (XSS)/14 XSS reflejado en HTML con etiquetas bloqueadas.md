En esta clase nos enfrentamos a un entorno con XSS reflejado protegido por un firewall que bloquea la mayoría de etiquetas HTML y atributos comunes. El objetivo es encontrar una combinación que permita ejecutar código sin intervención del usuario, pese a las restricciones impuestas.

La funcionalidad vulnerable es un buscador, donde el valor introducido se refleja directamente en el contenido HTML. Intentos clásicos de inyección son rechazados, por lo que utilizamos una estrategia sistemática con ayuda de Burp Suite.

Con Burp Intruder, realizamos una prueba automatizada enviando distintas etiquetas HTML y atributos, observando cuáles generan respuestas válidas. Detectamos que la etiqueta body y el atributo onresize no son filtrados. A partir de ahí, construimos un vector usando un contenedor invisible que al cargarse activa un evento de cambio de tamaño, el cual ejecuta directamente una función del navegador.

La prueba se completa al entregar el vector a una víctima a través de un servidor de explotación, validando así que la ejecución ocurre sin necesidad de clics o interacción adicional.

Este laboratorio muestra cómo es posible evadir sistemas de defensa si se analizan sus patrones de filtrado y se utilizan vectores alternativos cuidadosamente seleccionados.

Aqui tenemos el link de los tags
https://portswigger.net/web-security/cross-site-scripting/cheat-sheet

Solucion
Esto paso que cuando nosotros ponemos el script nos sale una ventana emergente por lo que tiene bastante filtros
![[Pasted image 20250710160426.png]]
entonces vamos a utilizar BS en el apartado de intruder priemero ponemos en el apartado de busquedad esto <script>alert(0)</script>
u luego interceptamos esto en la url
![[Pasted image 20250710161221.png]]
abrimos el BS y mandamos esta peticion al intruder ponemos las rexpectivos <> en apartado de GET
y vamos a seleccionar el apartado de test y le damos add para hacer un payload
![[Pasted image 20250710161617.png]]
entonces lo que sigue es copiar la lista del cheat para poder pegarla en el payload
![[Pasted image 20250710161901.png]]
![[Pasted image 20250710161927.png]]
quitamos la casilla marcada que se esta mas abajo y le damos start attack
y podemos ver que en ataque la etiqueta body le gusta
![[Pasted image 20250710163256.png]]
por lo cual en la url en ves de ponerlo en test podemos ponerle body e volverlo a interceptar pero esta ves lo mandamos al repeter y ponemos de nuevo las etiquetas <>
entonces le agregamos una etiqueta mas para mandarlo a introduer y hacer un ataque con el payload pero esta ves de los evento en cheet
![[Pasted image 20250710164612.png]]
y el campo desconozco le damos add y pegamos la lista recordar que esta ves va hacer  el de los eventos
![[Pasted image 20250710164743.png]]
Desmarcamos nuevamente la casilla de hasta abajo y iniciamos ataque
![[Pasted image 20250710164922.png]]

Como podemos ver nosotros podemos ver en la cadena bastantes codigos 200 en este caso podemos utilizar onresize
![[Pasted image 20250710170123.png]]
y la url quedaria asi para mandarselo a nusetro objetivo
<iframe src="https://0a59004c04e612a08323326800150063.web-security-academy.net/?search=<body onresize=print()>"></iframe>
y el exploid quedaria asi
<iframe src="https://0a59004c04e612a08323326800150063.web-security-academy.net/?search=<body onresize=print()>" onload=this.style.width='100px></iframe>
esta url es la que le debemos mandar a nuestra victima







