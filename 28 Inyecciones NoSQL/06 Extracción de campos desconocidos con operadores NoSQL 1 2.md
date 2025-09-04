En esta clase aprendemos a utilizar el operador **$where** junto a ‘**Object.keys(this)**‘ para enumerar propiedades ocultas dentro de documentos JSON en MongoDB. Mediante Burp Intruder y un ataque Cluster bomb, iteramos sobre posiciones y caracteres posibles, identificando con precisión el nombre de los campos como username, email, y el de reseteo de contraseña.

Este enfoque revela cómo se puede mapear el esquema interno de la base de datos sin acceso directo a ella.

Solucion
no nos dan credenciales asi que vamos a interceptar el login y lo mandamos al repeater
![Pasted_image_20250902013444.png](Imagenes/Pasted_image_20250902013444.png)
![Pasted_image_20250902014123.png](Imagenes/Pasted_image_20250902014123.png)
