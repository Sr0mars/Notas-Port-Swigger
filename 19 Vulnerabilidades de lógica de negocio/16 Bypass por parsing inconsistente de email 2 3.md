Aquí aprovechamos la diferencia entre cómo el validador del servidor y el sistema de entrega de correo interpretan una dirección en **UTF-7**. Registramos una cuenta que visualmente termina en **@ginandjuice.shop**, pero que en realidad el servidor de correo interpreta como perteneciente a nuestro dominio de exploit.

Como resultado, recibimos el correo de activación, validamos la cuenta y obtenemos acceso a la plataforma.

Solucion
entonces en este punto tenemos que probar varios RCEs para ver cual es el que acepta el servidor
primera prueba
![[Pasted image 20250829021752.png]]
nope
![[Pasted image 20250829021809.png]]
segunda prueba
![[Pasted image 20250829021910.png]]
nope
![[Pasted image 20250829021926.png]]
tercera prueba
![[Pasted image 20250829022004.png]]
en este si nos dejo :D
![[Pasted image 20250829022026.png]]
