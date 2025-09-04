En esta clase llevamos a cabo un ataque avanzado de HTTP request smuggling para lograr un web cache poisoning. Usamos la diferencia de interpretación entre el front-end y el back-end para inyectar una redirección maliciosa en la caché del servidor. Al lograr que el fichero JavaScript ‘**tracking.js**‘ apunte al exploit server, conseguimos que el navegador de la víctima cargue un payload con ‘**alert(document.cookie)**‘. Se requiere repetir el ataque varias veces para sincronizarlo con las solicitudes simuladas del usuario víctima.

Solucion
Interceptamos y ponemos el payload
![Pasted_image_20250809233545.png](/Imagenes/Pasted_image_20250809233545.png)
### **Objetivo del payload**

Este tipo de payload se usa para:

- **HTTP desynchronization attacks**, como envenenar cachés, inyectar peticiones falsas o robar datos de otros usuarios.
    
- Aprovechar que frontend y backend interpretan de forma distinta la longitud y el formato del cuerpo.
    

En resumen, **estás viendo un ejemplo de "CL.TE" smuggling** (Content-Length vs Transfer-Encoding), donde el cliente envía ambos encabezados para generar confusión entre servidores intermedios.

En resumen:  
Este payload aprovecha una **confusión entre `Content-Length` y `Transfer-Encoding`** para que el primer servidor y el backend interpreten distinto dónde termina la petición.

El resultado es que logras **inyectar una segunda petición HTTP** dentro de la primera, engañando al backend para que la procese sin que el frontend se dé cuenta.

Básicamente:

1. El frontend cree que la petición termina antes.
    
2. El backend sigue leyendo y ejecuta tu “petición escondida”.
    
3. Esto se usa para manipular respuestas, envenenar caché o robar información.