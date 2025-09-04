En esta clase vemos una de las aplicaciones más conocidas de la inyección SQL: **eludir la autenticación en un formulario de login**.

La aplicación es vulnerable porque inserta directamente los valores introducidos por el usuario en una consulta SQL que verifica las credenciales. El objetivo es manipular esa consulta para forzar el acceso como administrador, sin necesidad de conocer la contraseña.

Para ello, se intercepta la solicitud de inicio de sesión con Burp Suite y se modifica el valor del parámetro ‘username’, dándole el siguiente valor:

- **administrator’–**

Esto cierra prematuramente la cadena del nombre de usuario y comenta el resto de la consulta, incluyendo la comprobación de la contraseña. El resultado es que el sistema nos deja pasar como si hubiéramos introducido credenciales válidas.

**Quédate con esto**: Las entradas del usuario nunca deben insertarse directamente en consultas SQL. Si lo hacen, pueden ser manipuladas para saltarse controles críticos como la autenticación.
![[Pasted image 20250701144400.png]]
Solucion
'test' or 1=1-- -

![[Pasted image 20250701144653.png]]