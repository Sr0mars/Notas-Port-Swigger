En esta clase trabajamos con una vulnerabilidad de inyección SQL que se encuentra en la funcionalidad de consulta de stock, la cual recibe datos en formato XML. La clave está en el parámetro ‘**storeId**‘, donde se inyectan instrucciones SQL directamente dentro del cuerpo XML de una petición POST.

Inicialmente identificamos que el valor de ‘**storeId**‘ es evaluado por el backend, permitiendo realizar operaciones como ‘**1+1**‘. Luego intentamos una inyección clásica mediante ‘**UNION SELECT**‘, pero la aplicación bloquea el intento, presumiblemente por un sistema WAF (Web Application Firewall).

Para evadir este filtro, aplicamos codificación de entidades XML (por ejemplo, hexadecimal o decimal), utilizando herramientas como la extensión **Hackvertor** en Burp Suite. Este bypass permite que el payload pase desapercibido y sea ejecutado por el backend.

A través de prueba y error, determinamos que la consulta original solo permite devolver una columna, por lo que concatenamos ‘**username**‘ y ‘**password**‘ con un separador (~) para extraer los datos de la tabla ‘**users**‘ en una sola columna.

Finalmente, utilizamos las credenciales obtenidas para iniciar sesión como ‘**administrator**‘ y resolver el laboratorio.

Esta lección muestra cómo técnicas de evasión pueden ser aplicadas a vectores no tradicionales, como peticiones en XML, destacando la importancia de adaptar los ataques al formato de entrada y a las defensas activas del sistema.

Solucion 
La vulnerabilidad se presenta en el apartado de los articulos dandole al boton primero tener encendido el BS y despues activar el foxy proxy despues de eso tenemos que presionar el boton para que nos mande la peticion al BS

en este caso tenemos que jugar con el codigo del boton dentro del BS
![[Pasted image 20250704145456.png]]
y vamos a instalar una extencion la cual nos va ayudar para este lab
![[Pasted image 20250704150215.png]]
lo que hace esta extencion es representar otra cadena en otro formato
seleccionamos la cadena le damos clic derecho y luego (puede ser hex o dec)![[Pasted image 20250704150439.png]]

y cuando lo mandamos no hay ningun problema 
![[Pasted image 20250704150645.png]]
ahora probaremos
union select username from users where username='administrator'
![[Pasted image 20250704150910.png]]
union select username from users
![[Pasted image 20250704150948.png]]
union select username ||';'||password from users
![[Pasted image 20250704151105.png]]
y ya con esto nos logeamos
