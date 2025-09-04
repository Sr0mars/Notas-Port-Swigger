En esta última parte, realizamos el ataque completo de HTTP/2 request tunnelling. Inyectamos una petición GET camuflada hacia /admin con las cabeceras de autenticación previamente obtenidas, simulando ser el administrador. Aprovechamos el downgrade de protocolo para túnelar una solicitud HTTP/1.1 y acceder a funciones restringidas, como la eliminación del usuario carlos.

A pesar de que las respuestas del servidor puedan parecer erróneas, el ataque se completa con éxito y el laboratorio queda resuelto.

Solucion
Entonces aqui ya seria jugar con el CL en este caso le vamos a aumentar a 160 para que nos de mas informacion
![[Pasted image 20250811172802.png]]
Entonces estas cabeceras se las podemos colar a la otra consulta
![[Pasted image 20250811172918.png]]
entonces esto lo copiamos y lo pegamos en el otro payload para poder ejecutar la informacion
![[Pasted image 20250811184658.png]]
se pone en login por que tiene mas cantidad de bytes
asi quedaria
![[Pasted image 20250811184731.png]]
ya solo copiamos la direccion
![[Pasted image 20250811184759.png]]
![[Pasted image 20250811184817.png]]
pese el mensaje la consulta se consiguio
![[Pasted image 20250811184957.png]]


