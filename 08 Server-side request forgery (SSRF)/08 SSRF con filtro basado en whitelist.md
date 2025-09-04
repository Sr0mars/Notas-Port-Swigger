En esta clase trabajamos con un escenario en el que se ha implementado una defensa basada en lista blanca para mitigar ataques SSRF. A pesar de esta protección, conseguimos acceder a un endpoint interno aprovechando cómo el servidor interpreta las URLs con credenciales embebidas.

Comenzamos probando distintas variantes del parámetro ‘**stockApi**‘, observando cómo la aplicación extrae y valida el hostname. Tras verificar que se aceptan URLs con formato de usuario, utilizamos técnicas de doble codificación para manipular el valor del hostname y hacer que el servidor interprete la URL de forma diferente a como lo hace la validación.

Gracias a esto, logramos redirigir la petición al endpoint de administración alojado en ‘**localhost**‘, y ejecutamos la acción de eliminar al usuario objetivo. Esta clase muestra cómo se pueden eludir filtros aparentemente robustos manipulando los componentes de una URL.

Solucion
Interceptamos con BS y vemos que esta apuntando a un servidor interno
![Pasted image 20250804204207.png](imagenes/Pasted image 20250804204207.png)

aqui no sirve nada de lo que realizamos anterior mente por que nos obliga que mantega la url que estaba al principio
![Pasted image 20250804204424.png](imagenes/Pasted image 20250804204424.png)
asi que lo podemos hacer es autenticarnos desde la url
![Pasted image 20250804204751.png](imagenes/Pasted image 20250804204751.png)
asi que el payload quedaria asi (http://localhost:80%2523@stock.weliketoshop.net/admin/delete?username=carlos)

Explicacion
## 🧩 Paso a paso: Decodificación

### Paso 1: Decodificar `%2523`

El valor `%2523` es **URL-encoded**.

- `%25` es el código de **`%`**, así que:
    
    - `%2523` → `%23`
        
    - `%23` → `#` (carácter de fragmento en URL)
        

Así que la URL queda como:

perl

`http://localhost:80%23@stock.weliketoshop.net/admin/delete?username=carlos`

---

### Paso 2: Interpretación de partes de la URL

Según el estándar de URLs, la estructura es:

pgsql

`scheme://[user[:password]@]host[:port]/path?query#fragment`

En esta URL:

- `scheme`: `http`
    
- `user`: `localhost`
    
- `password`: `80#` (dependiendo del parser)
    
- `host`: `stock.weliketoshop.net`
    
- `path`: `/admin/delete`
    
- `query`: `username=carlos`

