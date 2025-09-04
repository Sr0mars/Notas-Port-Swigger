El laboratorio plantea un escenario en el que un endpoint sensible (/accountDetails) devuelve información privada —como la clave API del usuario— y permite solicitudes de origen cruzado reflejando el valor de la cabecera Origin. Esto significa que el servidor confía ciegamente en cualquier origen que le envíe una solicitud, siempre y cuando también devuelva la cabecera Access-Control-Allow-Credentials: true, lo que permite el envío de cookies junto con la petición.

La clase demuestra cómo el atacante puede aprovechar esta configuración desde un servidor malicioso (el exploit server) para realizar una petición XMLHttpRequest al dominio objetivo usando ‘**withCredentials: true**‘. Al no haber un filtrado adecuado en el backend, el servidor refleja el origen del atacante como válido y responde con los datos sensibles. El código JavaScript malicioso lee la respuesta y redirige al atacante a una URL de registro con la clave extraída como parámetro.

Con esta técnica, el atacante puede robar información del administrador sin necesidad de inyecciones en el servidor víctima, simplemente manipulando la política de intercambio de recursos entre dominios que ha sido mal configurada.

Solucion
Lo primero que nos sale es que a la hora de logearnos nos aparece una apy key
![Pasted image 20250728201323.png](imagenes/Pasted image 20250728201323.png)
vamos a interceptarlo
le damos forward y despues lo mandamos al repeater vemos de primera que tenemos una peticion GET al account details
![Pasted image 20250728201626.png](imagenes/Pasted image 20250728201626.png)
![Pasted image 20250728202254.png](imagenes/Pasted image 20250728202254.png)
