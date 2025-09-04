En esta lección abordamos una inyección SQL ciega avanzada basada en tiempo. Aunque la aplicación no muestra respuestas distintas al ejecutar consultas, sí permite detectar comportamientos a través del retardo en la respuesta del servidor.

Partimos de una cookie ‘**TrackingId**‘ vulnerable que se inserta directamente en una consulta SQL. Aprovechamos esta inyección para condicionar la ejecución de la función ‘**pg_sleep**‘ en función del resultado de la consulta. Si la condición se cumple, la aplicación se retrasa; si no, responde al instante.

Inicialmente verificamos si existe el usuario ‘**administrator**‘. A partir de ahí, inferimos la longitud exacta de su contraseña mediante condiciones incrementales como ‘**LENGTH(password)>n**‘, observando el tiempo de respuesta.

Una vez conocida la longitud (20 caracteres), automatizamos el proceso con Burp Intruder, utilizando ‘**SUBSTRING()**‘ para probar carácter por carácter. Configuramos los ataques para ejecutarse en un solo hilo y comparamos los tiempos de respuesta para identificar los caracteres correctos.

Finalmente, reconstruimos la contraseña completa y accedemos con las credenciales del administrador, completando el laboratorio con éxito.

Solucion
En este caso no funciona ni el order by nada por lo que estamos a ciegas
lo primero seria identificar que tipo de base de datos es
tal y como parece es Postgres por lo el tiempo de espera que tenemos
![Pasted image 20250704121358.png](imagenes/Pasted image 20250704121358.png)
y lo que podemos hacer es meter otra querry utilizando(;) por lo que la querry va seguir funcionando esta querry lo que hace es validar si 1=1 es verdadero va tardar a cambia en caso si lo cambiamos a 2=1 recargara rapido, (1=1) es el correcto
![Pasted image 20250704122057.png](imagenes/Pasted image 20250704122057.png)
esto para validar si el usuario administrator es valido
![Pasted image 20250704122401.png](imagenes/Pasted image 20250704122401.png)
para validar el tamaño de la contraseña
![Pasted image 20250704122452.png](imagenes/Pasted image 20250704122452.png)
en este caso resulto ser 20
![Pasted image 20250704122520.png](imagenes/Pasted image 20250704122520.png)
para validar el primer caracter de la contraseña en esta caso es m
![Pasted image 20250704122645.png](imagenes/Pasted image 20250704122645.png)
para ello vamos a realizar un scrpit para facilitar la explotacion
