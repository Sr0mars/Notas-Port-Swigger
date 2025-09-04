Durante el proceso de login, interceptamos la respuesta que establece una cookie llamada ‘**Admin=false**‘.

Al modificarla a ‘**Admin=true**‘, obtenemos privilegios de administrador y accedemos al panel oculto en /admin. Desde ahí, eliminamos al usuario carlos para completar el laboratorio.
Solucion
interceptamos la el login
![Pasted image 20250815172855.png](imagenes/Pasted image 20250815172855.png)podemos ver que en la intercepcion viene con un false lo que significa que no tiene ningun tipo de encryptacion ni nada
![Pasted image 20250815173054.png](imagenes/Pasted image 20250815173054.png)
entonces en la web solo minupulamos al estructura a true
![Pasted image 20250815175616.png](imagenes/Pasted image 20250815175616.png)
y ya con eso tenemos acceso al admin
![Pasted image 20250815175658.png](imagenes/Pasted image 20250815175658.png)
