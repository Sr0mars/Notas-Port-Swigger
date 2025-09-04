La aplicación diferencia los permisos según el método HTTP. Observamos que un POST necesita privilegios, pero al cambiar el método a GET, el backend sigue procesando la solicitud sin aplicar el control adecuado. Al interceptar la petición original desde Burp y cambiar el método a GET, es posible promocionar a nuestro usuario sin ser administrador, aprovechando una validación deficiente basada únicamente en el verbo HTTP.

Solucion
si nosotros nos logeamos como admin podemos darle o quitarle privilegios al los usuarios
![[Pasted image 20250815191148.png]]
asi que vamos a interceptarlo el upgrade
![[Pasted image 20250815191344.png]]
Asi que ahora nos logeamos como wiener
![[Pasted image 20250815191445.png]]
y ahora vamos a tomar nuestra cookie de session y la vamos a pegar en la peticion de admin pero vemos que no podemos autorizar privilegios
![[Pasted image 20250815191640.png]]
entonces ahora vamos a cambiar el metodo
y cambiamos el usuario que estaba por wiener y cambiamos el downgrade por upgrade
![[Pasted image 20250815191750.png]]
![[Pasted image 20250815191848.png]]
