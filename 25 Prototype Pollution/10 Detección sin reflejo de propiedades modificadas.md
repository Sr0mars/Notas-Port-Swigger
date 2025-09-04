En esta clase exploramos cómo identificar una vulnerabilidad de server-side prototype pollution sin depender de la reflexión directa de propiedades inyectadas en la respuesta. Usamos como contexto una funcionalidad de cambio de dirección en una aplicación Node.js con Express, que fusiona sin control los datos recibidos.

Aprovechamos esto para inyectar un campo ‘**proto**‘ con una propiedad ‘**status**‘, lo que nos permite alterar el código de estado en respuestas de error generadas artificialmente. Comprobamos que, tras romper deliberadamente el formato del JSON, el servidor devuelve un código de error manipulado, lo que confirma que nuestra propiedad ha sido introducida en el prototipo.

Esta clase es útil para practicar técnicas no destructivas de detección en entornos donde no se puede validar visualmente el impacto de la contaminación.

Solucion
de igual manera nos logeamos e intercetamos esto
![[Pasted image 20250901002130.png]]
obtenemos esto
![[Pasted image 20250901002209.png]]
y la idea en este laboratorio es contaminar el objeto global vamos a primero hacer creando un error
![[Pasted image 20250901002818.png]]
por lo cual vamos a cambiar la propiedad status ,"__proto__":{"status":405}
![[Pasted image 20250901002953.png]]
no vemos nada pero si de igual forma forzamos un error
![[Pasted image 20250901003026.png]]
y vemos que se hereda el error que nosotros pusimos
![[Pasted image 20250901003102.png]]
