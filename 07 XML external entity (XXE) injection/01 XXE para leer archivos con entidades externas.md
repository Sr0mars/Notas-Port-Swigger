En esta clase resolvemos un laboratorio que permite la explotación de una vulnerabilidad XML External Entity (XXE) en una funcionalidad de comprobación de stock. Continuamos trabajando con peticiones XML personalizadas, donde aprovechamos la posibilidad de declarar entidades externas para acceder a archivos internos del sistema operativo.

En este caso, inyectamos una entidad que apunta al archivo /etc/passwd, el cual es devuelto en la respuesta cuando se intenta verificar un producto. Es una demostración clara de cómo una mala configuración del parser XML puede abrir la puerta a una fuga crítica de información en el servidor.

Solucion
Que es?
![Pasted_image_20250730190319.png](/Imagenes/Pasted_image_20250730190319.png)
La web
![Pasted_image_20250730190613.png](/Imagenes/Pasted_image_20250730190613.png)
vamos a interceptar con BS esta parte dandole al check stock
![Pasted_image_20250730190643.png](/Imagenes/Pasted_image_20250730190643.png)
podemos ver en el repeater que la peticion es correcta
![Pasted_image_20250730190857.png](/Imagenes/Pasted_image_20250730190857.png)
pero nostros podemos modificar poniendo una cadena de texto el cual si la modificamos nos dara un error
![Pasted_image_20250730190946.png](/Imagenes/Pasted_image_20250730190946.png)
y para resolver este laboratorio tendremos que poner este payload (<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>)
- Es un **payload de ataque XXE (XML External Entity)**.
    
- Intenta **leer el archivo `/etc/passwd`** del sistema donde se procesa el XML.
    
- Si la aplicación es vulnerable, al usar `&xxe;` en el XML, se insertará el contenido del archivo.
    
- Se usa para **robar información sensible** o hacer otros ataques (como DoS o escaneo interno).
    
- **Prevención**: deshabilitar entidades externas en el parser XML.

y esto se inyecta aqui
![Pasted_image_20250730192051.png](/Imagenes/Pasted_image_20250730192051.png)

