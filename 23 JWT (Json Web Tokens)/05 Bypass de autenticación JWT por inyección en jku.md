En esta clase explotamos una vulnerabilidad relacionada con el parámetro **jku** del encabezado de un JWT. Este parámetro permite al servidor obtener dinámicamente la clave pública desde una URL externa para verificar la firma del token. El fallo consiste en que el servidor no valida si esa URL pertenece a un dominio confiable.

Creamos un conjunto de claves (JWK Set) en un servidor que controlamos y colocamos nuestra clave pública en él. Luego generamos un JWT firmado con la clave privada correspondiente, indicando en el **jku** la ubicación de nuestra clave pública y configurando el token para suplantar al administrador.

El servidor acepta la clave, valida el token, y accedemos al panel de administración desde donde eliminamos al usuario Carlos. Este laboratorio demuestra cómo la confianza ciega en ubicaciones externas puede comprometer completamente la autenticación.

Solucion
nos logeamos y ahora vamos a interceptar este apartado tambien nos comparten un exploit server
![Pasted_image_20250831000621.png](/Imagenes/Pasted_image_20250831000621.png)
![Pasted_image_20250831000828.png](/Imagenes/Pasted_image_20250831000828.png)
aqui poca cosa se puede hacer pero podemos agregar una cabecera donde apunte a nuestro exploit server
ahora vamos a crear otra RSA KEY
pero esta ves le vamos a dar copu public key as JWK
![Pasted_image_20250831001142.png](/Imagenes/Pasted_image_20250831001142.png)
vamos a crear ina estructura para nuestro explot server
{
    "keys": [

    ]
}

y en el espacio del centro vamos a pegar la public key en el exploit
![Pasted_image_20250831001422.png](/Imagenes/Pasted_image_20250831001422.png)
le damos wiev exploit 
y el kid no lo vamos a copiar y lo vamos a pegar en el intercep
le damos a sync
![Pasted_image_20250831001938.png](/Imagenes/Pasted_image_20250831001938.png)
le damos ok
y ya nada mas copiamos la cookie


