En este laboratorio, el token CSRF está vinculado a una cookie (**csrfKey**), pero esta cookie no está realmente ligada a la sesión de usuario, lo que permite suplantar el valor.

Para explotarlo:

- Iniciamos sesión con un usuario y capturamos tanto el valor del **csrfKey** como el token CSRF.
- Probamos que el servidor acepta esos valores incluso cuando son usados por otro usuario, es decir, no hay una validación estricta entre token, cookie y sesión.
- Además, observamos que la funcionalidad de búsqueda refleja cabeceras **Set-Cookie**, lo que nos permite inyectar cookies arbitrarias en el navegador víctima.
- Montamos un exploit que:
    - Realiza una búsqueda maliciosa para setear la cookie csrfKey deseada.
    - Luego, una vez inyectada, envía el formulario con el token capturado, consiguiendo cambiar el email de la víctima.

Este tipo de fallo es un buen ejemplo de validaciones CSRF mal implementadas, donde la lógica del servidor es parcial o inconsistente.

Solucion
Pues lo primero seria logearnos con el correo que nos dan lo siguiente seria hacer cambio de correo pero interceptarlo con BS y mandarlo al repeater, vemos primero que existe una keycsrf
![[Pasted image 20250723195200.png]]
ahora tocaria interceptar un cambio a la otro correo aqui lo que podemos ver es que el hay una similitud en los csrf
![[Pasted image 20250723200035.png]]
asi que tocaria buscar donde encontramos eso o por donde podriamos mandar los csrf el uno del otro para ello vamos a interceptar en wiener la barra de busquedad
asi que lo que hacemos aqui es es darle a send antes lo enviamos por el repeater y bueno que obtenemos
![[Pasted image 20250723200431.png]]
vemos aqui que se esta mandando o setiando una cookie lo cual deriva en 