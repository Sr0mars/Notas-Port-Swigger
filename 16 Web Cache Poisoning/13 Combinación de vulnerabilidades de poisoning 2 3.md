Aunque no se puede atacar directamente a usuarios en inglés, es posible obligar a la víctima a cambiar de idioma. El sistema establece el idioma mediante un endpoint como ‘**/setlang/es**‘, que normalmente devuelve una respuesta con ‘**Set-Cookie**‘ y no se almacena en caché. Sin embargo, si se usa ‘**X-Original-URL: /setlang\es**‘, el servidor hace una redirección normalizada a ‘**/setlang/es**‘, sin incluir cabeceras problemáticas. Este 302 sí es cacheable.

El objetivo de esta clase es explotar esta normalización para almacenar en la caché una redirección que fuerza a todos los visitantes a navegar en español, abriendo la puerta al XSS preparado en la clase anterior.

Solucion
asi que para empezar a vulnerar podemos probar las cabeceras que anteriormente hemos utilizado
![[Pasted image 20250822185618.png]]
por lo cual sabemos que si funciona podemos poner la url de nuestro exploit server por lo cual pasamos a modificar haciendo referencia al url json que se va emplear
y en el exploit hacer el formato de igual forma json para que tengamos problema recordar poner el CORS(Access-Control-Allow-Origin: *)
![[Pasted image 20250822190045.png]]
de tal manera que tenemos que configurar ahora el BS hacien referencia hacia localized que es donde hace el redirect
![[Pasted image 20250822190512.png]]
asi que con esto recargamos la pagina le damos en spanish y vemos el mensaje
![[Pasted image 20250822190711.png]]
pero ahora nosotros necesitamos redirigir al usuario al localized =1 cuando el este en el home para esto vamos a utilizar otra cabecera (X-Original-URL: /setlang\es) que justamente hace que se cache el localized
