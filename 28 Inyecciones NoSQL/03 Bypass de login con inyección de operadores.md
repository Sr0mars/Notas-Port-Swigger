En esta clase vemos cómo el uso inseguro de operadores NoSQL en consultas MongoDB permite eludir la autenticación. Analizamos el comportamiento de los campos **username** y **password** al inyectar operadores como ‘**$ne**‘ (distinto de) o ‘**$regex**‘. Utilizando expresiones regulares, conseguimos seleccionar la cuenta del administrador sin conocer sus credenciales.

Al explotar esta lógica insegura, logramos acceder al panel como admin y resolver el laboratorio.

Solucion
interceptamos el login pero dropeamos
![Pasted_image_20250902003130.png](Imagenes/Pasted_image_20250902003130.png)
vemos que cuando le damos send nos manda un estado 302
![Pasted_image_20250902003221.png](Imagenes/Pasted_image_20250902003221.png)
si la contraseña es incorrecta y le damos send el estado es 200
![Pasted_image_20250902003330.png](Imagenes/Pasted_image_20250902003330.png)y como es mongo db podemos modificar el request dado que es posible que por medio de regex nos interpreta la consulta
![Pasted_image_20250902003636.png](Imagenes/Pasted_image_20250902003636.png)
![Pasted_image_20250902004231.png](Imagenes/Pasted_image_20250902004231.png)
![Pasted_image_20250902004249.png](Imagenes/Pasted_image_20250902004249.png)
![Pasted_image_20250902004310.png](Imagenes/Pasted_image_20250902004310.png)
¿Por qué es importante?
Este tipo de consulta es común en pruebas de seguridad, especialmente en ataques de NoSQL Injection, donde se intenta manipular la lógica de autenticación enviando estructuras como esta en campos de formularios.
Por ejemplo, si una aplicación no valida correctamente los datos enviados, un atacante podría enviar esta estructura como parte del login para intentar acceder sin conocer la contraseña real.

ya solo
le damos click derecho request in browser in original session nos copiamos lo que nos da y lo pegamos en una nueva ventana
![Pasted_image_20250902004534.png](Imagenes/Pasted_image_20250902004534.png)
