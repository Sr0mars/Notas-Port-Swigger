En esta clase se estudia un ataque de Forced OAuth Profile Linking, donde el atacante aprovecha la falta de validación del parámetro state en el flujo OAuth para vincular su propia cuenta social a la sesión de otro usuario, en este caso, la cuenta del administrador.

El sitio web ofrece la posibilidad de enlazar un perfil social a una cuenta local ya existente, permitiendo así que el usuario pueda autenticarse mediante OAuth en el futuro. El problema es que esta vinculación no está protegida contra ataques CSRF: el endpoint ‘**/oauth-linking?code=…**‘ no valida si el código de autorización fue solicitado por el mismo usuario que va a asociar la cuenta.

El atacante completa el flujo de autorización con su propia cuenta social, pero intercepta y guarda el enlace final que contiene el código de autorización. Luego, construye un exploit HTML que contiene un iframe apuntando a dicho enlace, y lo envía al administrador mediante el exploit server. Como el administrador tiene una sesión activa en la web, su navegador realiza la petición al endpoint de vinculación, usando el código robado del atacante y asociando su cuenta social con la cuenta del administrador.

Posteriormente, el atacante simplemente inicia sesión usando su perfil social y accede directamente a la cuenta del administrador. Una vez dentro, puede acceder al panel de administración y eliminar al usuario carlos, completando así el laboratorio.

Este escenario demuestra cómo un descuido en el manejo de tokens OAuth y la ausencia de medidas anti-CSRF pueden poner en riesgo cuentas privilegiadas.

Solucion
nos logeamos 
![Pasted image 20250830002509.png](imagenes/Pasted image 20250830002509.png)
si le damos a attach nos redirige a la red social
![Pasted image 20250830002617.png](imagenes/Pasted image 20250830002617.png)
algo que vemos en la peticiones del historico es una validacion de codigo
![Pasted image 20250830002936.png](imagenes/Pasted image 20250830002936.png)
asi que vamos a interceptar el attach y vamos a ver donde se manda la solicitud
![Pasted image 20250830003254.png](imagenes/Pasted image 20250830003254.png)
vamos a darle forward hasta que ve amos la solicitud
y a este
![Pasted image 20250830003358.png](imagenes/Pasted image 20250830003358.png)
vamos a darle click derecho copiamos la url y vamos a dropearla
y esa url la vamos a copiar en nuestro exploit server por medio de iframe (<"iframe src="https://0aaf00e1030da514806462870027000c.web-security-academy.net/oauth-linking?code=Heux4Jx3j3kiFMqeaUvJF7cC-Ij8j7AOvpdrZivI6Wl"></iframe">)
![Pasted image 20250830003657.png](imagenes/Pasted image 20250830003657.png)
tal que le damos deliver exploit y nos vamos al home desde otra ventana
y nos deslogeamos y si nos authenticamos desde el boton de social media
![Pasted image 20250830003829.png](imagenes/Pasted image 20250830003829.png)
y nos sale el admin panel
![Pasted image 20250830005034.png](imagenes/Pasted image 20250830005034.png)
