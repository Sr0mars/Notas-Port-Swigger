Este laboratorio demuestra cómo un sistema de autenticación en dos pasos puede ser comprometido si la lógica de verificación no está correctamente implementada. Aunque la aplicación genera un código 2FA único para cada usuario, el endpoint que lo valida permite especificar explícitamente para qué usuario se verifica el código, lo que abre la puerta a ataques dirigidos.

Primero, generarás un código 2FA válido para Carlos manipulando el parámetro **verify**. Luego, enviarás un código inválido en tu propio flujo de autenticación para reutilizar el endpoint de validación, y mediante Burp Intruder realizarás un ataque de fuerza bruta sobre el código de Carlos. Una vez encuentres el código correcto, obtendrás acceso a su cuenta y podrás visitar su panel para resolver el laboratorio.

Solucion
Viendo la pagina y pasandola en el BS podemos ver que es posible que no se pueda evadir el 2FA esto en la peticion GET
![[Pasted image 20250820200858.png]]
en el codigo se puede ver un verify asi que este es posible que se pueda cambiar a carlos
![[Pasted image 20250820200954.png]]
igual esto se puede aplicar para la peticion POST pero aqui vemos que se aplica un codigo mfa-code que esta en la parte de abajo por lo cual se puede aplicar BF asi que estas 2 las mandamos al repeter y la peticion post al intruder tambien
asi que lo que sigue es crearnos un diccionario
![[Pasted image 20250820201520.png]]
cargamos el payload y configuramos el grep
![[Pasted image 20250820201704.png]]
ya solo mandamos la solicitud y inicimaos el ataque
![[Pasted image 20250820201740.png]]
y al final nos da un coockie de session la copiamos y pegamos
![[Pasted image 20250820203739.png]]


