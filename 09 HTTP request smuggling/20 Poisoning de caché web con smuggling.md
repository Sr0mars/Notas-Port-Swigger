En esta clase realizamos un ataque de web cache poisoning aprovechando una vulnerabilidad de HTTP request smuggling. Al manipular el encabezado Host de una petición smuggleada, conseguimos que el servidor almacene en caché una redirección hacia el exploit server, desde donde se sirve un archivo JavaScript con el payload ‘**alert(document.cookie)**‘.

Este ataque requiere sincronizarse con las peticiones del usuario víctima y puede requerir varios intentos hasta lograr que el recurso ‘**tracking.js**‘ se envenene correctamente.

Solucion
Entonces vamos a interceptar la el home a la raiz y hacemos las configuracion del method y el http 1.1
![Pasted image 20250810200456.png](imagenes/Pasted image 20250810200456.png)
bueno buscando en la pagina podemos ver que nos el post nos lleva hacia otra direccion que es next (se esta aplicando un redirect)
![Pasted image 20250810194228.png](imagenes/Pasted image 20250810194228.png)
Entonces ahora nosotros podemos cachear algun recurso como este
![Pasted image 20250810200618.png](imagenes/Pasted image 20250810200618.png)
y esto nos podemos aprovechar de para pornerlo en el payload
![Pasted image 20250810200434.png](imagenes/Pasted image 20250810200434.png)
### Qué está pasando aquí

- **Transfer-Encoding: chunked** y **Content-Length** en la misma petición generan ambigüedad.
    
    - Algunos servidores priorizan **Content-Length**.
        
    - Otros priorizan **Transfer-Encoding**.
        
- El cuerpo comienza con `0\r\n\r\n`, que en codificación _chunked_ significa **"no hay más datos"** → la petición _termina_ según el servidor que procese chunked.
    
- Justo después, sin cerrar la conexión, se mete otra petición HTTP:
### Qué se busca lograr

Si el **frontend** interpreta `Transfer-Encoding: chunked` y cree que el request termina en `0\r\n\r\n`, pero el **backend** interpreta `Content-Length: 137` y espera más datos, entonces:

- El backend procesará la segunda parte (`GET /post/next?...`) como **una petición separada**.
    
- Esto permite:
    
    - **Bypass de filtros** en el frontend.
        
    - **Cache poisoning**.
        
    - **Obtención de contenido no autorizado**.
        
    - **Explotar rutas internas** (SSRF interno, manipulación de sesión, etc.).


En resumen:

Ese _payload_ es un **HTTP Request Smuggling** que:

- Envía **dos encabezados conflictivos** (`Content-Length` y `Transfer-Encoding: chunked`) para crear confusión.
    
- Cierra el cuerpo _chunked_ con `0\r\n\r\n` y **oculta dentro** una segunda petición `GET /post/next?postId=3`.
    
- Hace que el **frontend** crea que la petición termina antes, pero el **backend** siga leyendo y procese la segunda petición **sin pasar por los filtros**.
    

📌 **Objetivo**: inyectar y ejecutar una petición encubierta directamente en el backend, eludiendo validaciones o accediendo a recursos no autorizados.

