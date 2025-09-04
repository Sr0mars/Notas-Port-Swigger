En esta clase se aborda un bypass de autenticación mediante el uso indebido del flujo implícito de OAuth, donde el error se encuentra en cómo la aplicación cliente valida la identidad del usuario tras completar el proceso de autorización.

Durante el flujo OAuth, el usuario inicia sesión a través de un proveedor externo (por ejemplo, una red social), que devuelve al cliente un token junto con información básica del usuario autenticado. La aplicación cliente luego usa estos datos para autenticar internamente al usuario en su sistema.

Sin embargo, en este laboratorio, la validación es deficiente: la aplicación confía ciegamente en la dirección de correo enviada por el cliente en el cuerpo de la solicitud POST a /authenticate, sin comprobar que ese correo coincida con el asociado al token recibido del proveedor OAuth.

Este fallo permite que un atacante capture la solicitud de autenticación legítima (por ejemplo, como wiener@…), y la modifique cambiando el campo email por el de la víctima (**carlos@carlos-montoya.net**), mientras mantiene el token válido. Al reenviar esta solicitud, la aplicación interpreta erróneamente que el token pertenece a Carlos, y le otorga acceso sin necesidad de contraseña.

Este escenario refleja un caso realista de mala implementación de OAuth, donde la confianza en datos manipulables por el cliente puede tener consecuencias críticas.

Solucion
![Pasted_image_20250829224030.png](Imagenes/Pasted_image_20250829224030.png)
La Web:
![Pasted_image_20250829233701.png](Imagenes/Pasted_image_20250829233701.png)
vamos a my account
se tramita esto
![Pasted_image_20250829233829.png](Imagenes/Pasted_image_20250829233829.png)
y este es el login podemos ver que cambia la url
![Pasted_image_20250829233943.png](Imagenes/Pasted_image_20250829233943.png)
nos logeamos y nos sale esto
![Pasted_image_20250829234017.png](Imagenes/Pasted_image_20250829234017.png)
y nos regresa al home podemos ver que la url ya es la normal
![Pasted_image_20250829234040.png](Imagenes/Pasted_image_20250829234040.png)
y si le damos a my account podemos ver que ya es normal la peticion y ahi nos sale nuestra info
![Pasted_image_20250829234133.png](Imagenes/Pasted_image_20250829234133.png)
si nos vamos al historico y vemos una de las peticiones POST podemos ver que se esta tramitando informacion
![Pasted_image_20250829234452.png](Imagenes/Pasted_image_20250829234452.png)
lo vamos a mandar al repeater
asi que lo que vamos hacer es realizar cambio y vamos a poner el correo de carlos y en el username ponemos a carlos
le damos a send y vemos que no se a tramitado ningun error
![Pasted_image_20250829234813.png](Imagenes/Pasted_image_20250829234813.png)
algo que podemos hacer en BS es click derecho request in browser y le damos en in original session esto lo que hara es evitar tramitar la cookie en la pagina osea no tenemos que copiar y pegar la cookie en la pagina
nos da una url la copiamos y la pegamos en el navegador
![Pasted_image_20250829235106.png](Imagenes/Pasted_image_20250829235106.png)


