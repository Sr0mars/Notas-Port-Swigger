La última parte del ataque requiere mantener envenenadas simultáneamente dos rutas cacheables: una que contiene el JSON de traducciones malicioso y otra que redirige al usuario al idioma español. Esto se logra enviando primero la petición con ‘**X-Forwarded-Host**‘ para cachear el JSON malicioso, y después otra con ‘**X-Original-URL: /setlang\es**‘ para cachear la redirección.

Cuando el usuario accede a la página principal, será redirigido al entorno en español y cargará automáticamente el JSON con el payload, disparando el ‘**alert(document.cookie)**‘. Esta sincronización entre el contenido cacheado y el comportamiento del navegador resuelve el laboratorio con éxito.

Solucion
asi que en otra direccion de raiz con el BS ponemos la cabecera
![[Pasted image 20250822192142.png]]
Asi que en resumen spameamos el send de las 2 consultas
1.-
![[Pasted image 20250822192219.png]]
2.-
![[Pasted image 20250822192236.png]]
asi que una vez terminandolo solo recargamos la pagina
![[Pasted image 20250822192323.png]]
