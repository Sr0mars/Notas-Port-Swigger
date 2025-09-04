En esta clase descubrimos un fallo en la verificación de JWTs donde el servidor acepta tokens sin firma si el campo **alg** se define como **none**. Aprovechamos esta configuración insegura para crear un token completamente manipulado: modificamos el campo **sub** para suplantar al usuario administrador, establecemos el algoritmo a **none** y eliminamos la firma dejando sólo el encabezado y el payload separados por un punto.

A pesar de carecer de firma, el servidor acepta el token y nos da acceso al panel de administración, desde donde eliminamos al usuario Carlos. Este laboratorio demuestra por qué permitir alg: none es una práctica peligrosa y cómo puede ser aprovechada por un atacante para evitar autenticaciones basadas en JWT.

Solucion
vemos que no nos podemos ir a la seccion admin lo interceptamos
![[Pasted image 20250830230942.png]]
y bueno si miramos la cookie vemos que tenemos un alg y un digito en el digito lo podemos modificar como none
![[Pasted image 20250830231227.png]]
![[Pasted image 20250830231307.png]]
en la siguiente parte vamos a cambiar wiener por administrator
![[Pasted image 20250830231354.png]]
y si ahora eliminamos toda la parte de la firma
![[Pasted image 20250830231435.png]]
y nos copiamos todo ![[Pasted image 20250830231525.png]]
pegamos en la session nos lleva directamente al admin panel
![[Pasted image 20250830231703.png]]
