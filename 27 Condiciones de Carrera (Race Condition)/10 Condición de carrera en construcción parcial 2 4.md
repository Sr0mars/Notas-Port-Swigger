Utilizando Burp Suite, enviamos solicitudes de registro y confirmación en rápida sucesión, y observamos que las respuestas del servidor a las confirmaciones llegan siempre más rápido que las del registro. Esto indica que existe una diferencia de tiempos que puede explotarse.

Al probar múltiples combinaciones de registro y confirmación con nombres de usuario únicos y tokens inválidos, validamos que existe una pequeña ventana en la que el servidor acepta ciertas confirmaciones incluso si el token no ha sido definido todavía.

Este hallazgo confirma la existencia de una condición de carrera en la validación del correo electrónico.

Solucion
entonces que pasa que al momento de darle a send el servidor nos interpreta una respuesta que un token es invalido
![[Pasted image 20250901215202.png]]
pero que pasa si ponemos un array vacio
![[Pasted image 20250901215236.png]]
entonces es posible que esto considere un valor vacio
podemos hacer una prueba haciendo un grupo entre estas 2 pestañas obviamente cambiando el usuario por otro y mandandolos de forma paralela
![[Pasted image 20250901215630.png]]
lo cual nos da como respues que el confirmation es mas rapido en respuesta que el registration
asi que lo que podemos hacer es utilizar el turbo intruder
esto se aplica en el apartado de username asi que lo seleccionamos extencions  turbo intruder
y lo urlcodeamos
