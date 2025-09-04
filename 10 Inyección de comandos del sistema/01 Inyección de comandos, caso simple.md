En esta clase aprovechamos una vulnerabilidad de inyección de comandos del sistema operativo en el verificador de stock. Al modificar el parámetro ‘storeID’ con ‘**1|whoami**‘, logramos que el servidor ejecute el comando ‘**whoami**‘, revelando así el usuario actual del sistema.

Se trata de un ejemplo básico pero efectivo para entender cómo los datos del usuario pueden ser interpretados directamente por el sistema si no se filtran adecuadamente.

Solucion
La web:
![Pasted_image_20250813204846.png](/Imagenes/Pasted_image_20250813204846.png)
en este caso la vulnerabilidad se encuentra en el check stock entonces vamos a interceptarlo
![Pasted_image_20250813205036.png](/Imagenes/Pasted_image_20250813205036.png)
de primeras no sabemos como esta estructurada la pagina
![Pasted_image_20250813205223.png](/Imagenes/Pasted_image_20250813205223.png)
asi que para resolver el laboratorio unicamente tenemos que poner en el campo stodeID el ; whoami
![Pasted_image_20250813205623.png](/Imagenes/Pasted_image_20250813205623.png)

