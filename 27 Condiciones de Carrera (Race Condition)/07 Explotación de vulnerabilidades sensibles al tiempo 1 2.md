Esta clase se centra en el análisis de un sistema de generación de tokens de recuperación de contraseña que, aunque no presenta condiciones de carrera clásicas, es vulnerable por su dependencia de datos temporales previsibles, como marcas de tiempo.

Al comparar respuestas de múltiples solicitudes realizadas casi simultáneamente, descubrimos que se pueden generar tokens idénticos. Además, observamos que estos tokens no dependen del nombre de usuario, lo que abre la puerta a que un atacante utilice su propio enlace de recuperación para establecer la contraseña de otro usuario.

El foco de esta clase está en identificar el patrón de generación de tokens y demostrar que las solicitudes concurrentes pueden sincronizarse para explotar la vulnerabilidad.

Solucion
nos vamos al login y le vamos a dar forget password vemos que tenemos un email client
![Pasted image 20250901205421.png](imagenes/Pasted image 20250901205421.png)
seguido ponemos nuestro usuario y lo revisamos en el email client
![Pasted image 20250901205450.png](imagenes/Pasted image 20250901205450.png)
una vez que le damos click podemos ver en la url como se acontece data en el token que parece ser que es SHA-1
![Pasted image 20250901205516.png](imagenes/Pasted image 20250901205516.png)
y bueno nos vamos al historico vemos una peticion post de forgot password lo mandamos al repeater y si le damos a send
vemos que recibimos otro email y otro valor en el token
![Pasted image 20250901205602.png](imagenes/Pasted image 20250901205602.png)
![Pasted image 20250901205624.png](imagenes/Pasted image 20250901205624.png)
asi que lo que tenemos en el repeater lo vamos a mandar al repeater osea duplicar y vamos a crear un grupo y vamos a mandar las solicitudes de forma paralela
![Pasted image 20250901205729.png](imagenes/Pasted image 20250901205729.png)
y vemos que el tiempo de estas cuando se envian es de bastante tiempo por lo cual no se estan enviando de forma paralela
tab1
![Pasted image 20250901205750.png](imagenes/Pasted image 20250901205750.png)
tab2
![Pasted image 20250901205807.png](imagenes/Pasted image 20250901205807.png)
entonces lo que podemos hacer mandar una solicitud por get al forgot password lo vamos a interceptar
![Pasted image 20250901205843.png](imagenes/Pasted image 20250901205843.png)
![Pasted image 20250901210003.png](imagenes/Pasted image 20250901210003.png)
