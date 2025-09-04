En esta primera clase, se revisa el flujo de autenticación OAuth desde Burp Suite. Se descubre que el parámetro redirect_uri admite rutas como ‘**/../**‘, lo que permite manipular la URL de redirección final, manteniéndola dentro del mismo dominio pero apuntando a rutas no previstas por el servidor. Aunque el dominio del **redirect_uri** está correctamente validado, esta técnica de path traversal permite eludir la restricción sin desencadenar errores.

Este análisis es crucial para preparar la explotación posterior, donde el objetivo será redirigir el token OAuth del administrador hacia una ruta vulnerable que permita su recolección por parte del atacante.

Solucion
nos logeamos checamos el historico vemos el auth y el /me y lo mandamos al repeater
![[Pasted image 20250830193332.png]]
![[Pasted image 20250830193356.png]]
buscamos un redirect pero no se encuentra
buscando en los post ponemos un comentario checamos el hisotirico
![[Pasted image 20250830193453.png]]
vemos que se trata de un iframe lo mandamos al repeater
![[Pasted image 20250830193546.png]]