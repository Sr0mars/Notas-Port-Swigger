Al editar nuestra dirección de correo desde la cuenta, interceptamos la petición y añadimos el campo ‘**“roleid”:2**‘ al cuerpo JSON.

Esto modifica nuestro rol a administrador, permitiéndonos acceder al panel /admin y eliminar al usuario carlos, resolviendo el laboratorio.

Solucion
vamos a interceptar el my account
![[Pasted image 20250815180100.png]]
en la intercepcion podemos ver que el roleid es 1 pero nosotros necesitamos ser el 2
![[Pasted image 20250815180136.png]]
