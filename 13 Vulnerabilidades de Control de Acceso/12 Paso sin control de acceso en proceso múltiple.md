En esta lección observamos cómo una promoción de roles en la sección de administración requiere varias etapas.

Aunque la primera fase valida permisos, la segunda no lo hace correctamente. Al interceptar la solicitud de confirmación en Burp y reutilizarla con nuestra propia sesión y usuario, logramos promocionarnos a administrador sin tener privilegios. Un fallo crítico en la aplicación al no validar de nuevo quién realiza el segundo paso.

Solucion
Empezamos con lo mismo nos logeamos como admin y despues upgradeamos a alguien pero nos sale esta ventana
![Pasted image 20250815192057.png](imagenes/Pasted image 20250815192057.png)
![Pasted image 20250815192722.png](imagenes/Pasted image 20250815192722.png)
en esta parte cambiamos de metodo y pero tambien vamos a interceptar la del upgrade 
![Pasted image 20250815193437.png](imagenes/Pasted image 20250815193437.png)
asi que modificamos por wiener 
pero para ello ya nos hemos logeado en con wiener y copiamos lo cookie de session
asi que le damos en get pero nos sale 404 
entonces lo que podemos hacer es cambiar en hambas el metodo por post
![Pasted image 20250815193634.png](imagenes/Pasted image 20250815193634.png)
![Pasted image 20250815193648.png](imagenes/Pasted image 20250815193648.png)
![Pasted image 20250815193701.png](imagenes/Pasted image 20250815193701.png)
y lo conseguimos
