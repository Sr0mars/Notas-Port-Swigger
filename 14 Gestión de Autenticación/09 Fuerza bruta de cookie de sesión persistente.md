En este laboratorio, se explota una mala implementación del sistema de “Mantener la sesión iniciada”. La cookie utilizada para esta funcionalidad contiene el nombre de usuario y el hash MD5 de la contraseña, codificados en Base64. Esto permite construir manualmente cookies válidas si se conocen o se adivinan las credenciales del usuario.

Primero, se observa el formato de la cookie con una cuenta propia y se confirma que contiene el nombre de usuario seguido del hash MD5 de la contraseña. A partir de esta estructura, se puede automatizar la construcción de nuevas cookies usando una lista de contraseñas, aplicando los siguientes pasos: hashear cada contraseña con MD5, anteponer el nombre de usuario (Carlos), y codificar el resultado en Base64.

El ataque se lanza con Burp Intruder, configurando reglas de procesamiento de payloads y detectando el éxito de la intrusión al identificar elementos únicos de una sesión iniciada como “Update email” en la respuesta. Cuando esto ocurre, se confirma que la cookie generada pertenece a Carlos y se obtiene acceso a su cuenta.

SOLUCION

