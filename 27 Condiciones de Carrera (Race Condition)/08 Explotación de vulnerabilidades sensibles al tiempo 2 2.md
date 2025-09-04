Tras comprobar que el token generado para el reseteo de contraseña se basa en una marca de tiempo y no incluye el nombre de usuario, llevamos a cabo un ataque práctico. Usamos dos sesiones independientes para enviar solicitudes de reseteo casi al mismo tiempo: una para nuestro usuario y otra para carlos.

Si los tiempos de respuesta se alinean, ambas solicitudes reciben el mismo token. Como controlamos el enlace enviado a nuestro correo, podemos simplemente sustituir el nombre de usuario por carlos en la URL de recuperación y establecerle una nueva contraseña.

Esta clase demuestra cómo un fallo criptográfico combinado con una ejecución precisa puede derivar en una toma de cuenta completa.

Solucion
como podemos ver en la ultima imagen la cookie es la misma por lo que vamos a eliminar la cookie vemos tambien que existe un  csrf
![Pasted image 20250901210222.png](imagenes/Pasted image 20250901210222.png)
y vamos a volver a replicar la otra consulta post y en esa nueva consulta vamos a pegar el csrf token del la peticion get
![Pasted image 20250901210508.png](imagenes/Pasted image 20250901210508.png)
y tambien vamos a copiar el php session de la peticion get
![Pasted image 20250901210628.png](imagenes/Pasted image 20250901210628.png)
asi quedaria la tab de enmedio
![Pasted image 20250901210721.png](imagenes/Pasted image 20250901210721.png)
y si le damos a send podemos ver que los tiempo ya son casi iguales
tab1
![Pasted image 20250901210830.png](imagenes/Pasted image 20250901210830.png)
tab2
![Pasted image 20250901210853.png](imagenes/Pasted image 20250901210853.png)
y si hacemos varias pruebas y vamos al mismo tiempo checando el email client podemos ver que en algun punto nos mandara 2 iguales
![Pasted image 20250901211105.png](imagenes/Pasted image 20250901211105.png)
esto significa que nos ha arrastrado el mismo token
asi que si nos vamos al tab2 y modificamos al usuario esto lo que hara es que nos daria el mismo token solo que cambiariamos en la url en ves de wiener a carlos la tab1 se queda como wiener por que de esta manera nos mandara el correo a nuestro emailclient
![Pasted image 20250901211301.png](imagenes/Pasted image 20250901211301.png)
asi que en la tab2 le damos send checamos el email client
le vamos a dar click derecho y copiar url
![Pasted image 20250901211614.png](imagenes/Pasted image 20250901211614.png)
abrimos una nueva pestaña y vamos a cambiar de wiener a carlos
![Pasted image 20250901211705.png](imagenes/Pasted image 20250901211705.png)
le damos enter
y si no nos sale error nosotros podemos cambiar la contraseña de carlos
![Pasted image 20250901211741.png](imagenes/Pasted image 20250901211741.png)
por lo que ahora le cambiamos la contraseña nos logeamos y eliminamos a carlos
![Pasted image 20250901211857.png](imagenes/Pasted image 20250901211857.png)
