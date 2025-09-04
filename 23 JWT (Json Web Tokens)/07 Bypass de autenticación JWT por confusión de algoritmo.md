En esta clase nos enfrentamos a una implementación insegura de JWT que utiliza claves RSA para firmar y verificar tokens. Sin embargo, el servidor es vulnerable a un ataque de confusión de algoritmos: permite cambiar el algoritmo de firma a HS256, el cual utiliza una clave simétrica.

Aprovechamos que el servidor expone su clave pública en el endpoint ‘**/jwks.json**‘, y la usamos como si fuera la clave secreta para firmar un nuevo token con HS256. Luego modificamos el payload para suplantar al usuario administrador y firmamos el JWT con la clave pública, que el servidor acepta erróneamente.

Así accedemos al panel de administración y eliminamos al usuario Carlos. Esta clase demuestra cómo una mala configuración de los algoritmos aceptados en JWT puede anular por completo la seguridad del sistema.

Solucion
lo primero es buscar el endpoint que seria este (/jwks.json)
![Pasted_image_20250831013125.png](Imagenes/Pasted_image_20250831013125.png)
no lo vamos a llevar al terminal para verlo mejor
![Pasted_image_20250831013242.png](Imagenes/Pasted_image_20250831013242.png)
ahora nos logeamos y vamos a interceptar esto
![Pasted_image_20250831013405.png](Imagenes/Pasted_image_20250831013405.png)
una vez interceptado nos podemos ir a cambiarle administrator
![Pasted_image_20250831013524.png](Imagenes/Pasted_image_20250831013524.png)
despues nos vamos a la extencion de JWT y lo que podemos hacer es darle new key rsa y pegar la key rsa que nos daba el end point cual quedaria asi
![Pasted_image_20250831013902.png](Imagenes/Pasted_image_20250831013902.png)
y ahora nos regresamos al intruder y modificamos el alg para que sea simetrica para ello nos regresamos a la extencion y vamos a crear
![Pasted_image_20250831013956.png](Imagenes/Pasted_image_20250831013956.png)
pero antes nos regresamos
![Pasted_image_20250831014122.png](Imagenes/Pasted_image_20250831014122.png)
vamos a copiarlo com PEM y lo mandamos al decoder donde lo vamos a pasar a base64
![Pasted_image_20250831014215.png](Imagenes/Pasted_image_20250831014215.png)
lo que genero lo copiamos y creamos una nueva key symetrica y lo pegamos en la  "K"
![Pasted_image_20250831014311.png](Imagenes/Pasted_image_20250831014311.png)
nos regresamos al intercep y le damos sign le damos ok
![Pasted_image_20250831014424.png](Imagenes/Pasted_image_20250831014424.png)
ahora copiamos la cookie y la pegamos en la web
![Pasted_image_20250831014529.png](Imagenes/Pasted_image_20250831014529.png)

