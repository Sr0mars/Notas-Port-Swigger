En esta clase aprendemos cómo una aplicación intenta proteger funciones críticas usando el encabezado Referer. Aunque esto puede parecer una capa de seguridad, es fácilmente manipulable.

Aprovechamos esta debilidad para modificar la solicitud en Burp, falsificar el Referer y cambiar nuestro propio rol a administrador sin autorización legítima.

Un ejemplo clásico de por qué confiar en encabezados del cliente es una mala práctica.

Solucion
de igual manera nos logeamos como admin e interceptamos el admin panel
![Pasted image 20250815194208.png](imagenes/Pasted image 20250815194208.png)
modificamos de carlos por wiener
![Pasted image 20250815194513.png](imagenes/Pasted image 20250815194513.png)
nos logeamos ahora con wiener
y eso lo interceptamos (para copiarnos la cookie de session)
![Pasted image 20250815194702.png](imagenes/Pasted image 20250815194702.png)
![Pasted image 20250815194759.png](imagenes/Pasted image 20250815194759.png)
