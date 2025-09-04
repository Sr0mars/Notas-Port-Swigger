En este laboratorio explotarás una debilidad lógica en la protección contra fuerza bruta basada en IP. La aplicación bloquea temporalmente una IP tras tres intentos fallidos consecutivos, pero este contador se reinicia si se realiza un inicio de sesión válido antes de alcanzar el límite.

Aprovechando esta lógica, realizarás un ataque tipo pitchfork en Burp Intruder, alternando peticiones con tu propio usuario (válido) y contraseñas correctas, con intentos de acceso al usuario objetivo carlos usando contraseñas de un diccionario. Este patrón evita que el sistema bloquee tu IP y te permite forzar la contraseña de Carlos sin interrupciones. Al identificar la contraseña correcta, iniciarás sesión en su cuenta para completar el laboratorio.

Solucion
entonces esto que significa que tenemos 3 intentos asi que si en 2 fallamos y en ultimo ponemos bien las credenciales se reinicia por asi decirlo el contador de intentos
![[Pasted image 20250819211057.png]]
por lo caul con las credenciales de password y user vamos a crearnos un script que nos permita automatizar esto
![[Pasted image 20250819211153.png]]
![[Pasted image 20250819211216.png]]
entonces ahora vamos a interceptar una solicitud de login normal y la mandamos al intruder
![[Pasted image 20250819211344.png]]
