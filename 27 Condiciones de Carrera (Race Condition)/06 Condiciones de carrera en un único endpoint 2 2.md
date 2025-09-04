Una vez comprendido el comportamiento del endpoint vulnerable, pasamos a la acción. Diseñamos dos solicitudes paralelas: una que apunta a nuestra dirección de correo legítima, y otra a la dirección protegida **carlos@ginandjuice.shop**.

El objetivo es interferir en el instante justo en que el servidor genera el cuerpo del correo de confirmación, haciendo que se dirija a nosotros pero valide la dirección de Carlos. Si el ataque tiene éxito, tomamos control del rol administrativo asociado a esa cuenta y accedemos al panel de administración, donde procedemos a eliminar al usuario Carlos.

Esta clase ilustra el impacto real de este tipo de vulnerabilidad, al permitir un bypass completo del control de acceso a partir de una simple condición de carrera.

Solucion
entonces vamos a emplear un ataque
lo primero es cambia el correo y lo interceptamos
![Pasted_image_20250901202722.png](Imagenes/Pasted_image_20250901202722.png)
lo vamos a mandar al repeater pero esa misma solicitud la vamos a dropear
estando en el repeater vamos a volverlo a mandar al repeater pero en la segunda tab vamos a poner el correo de carlos
carlos@ginandjuice.shop
![Pasted_image_20250901203138.png](Imagenes/Pasted_image_20250901203138.png)
y vamos a crear un grupo de tal manera que lo vamos a mandar de forma paralela
![Pasted_image_20250901203233.png](Imagenes/Pasted_image_20250901203233.png)
y esto es aprueba error mandamos la solicitud y vemos en el correo si existe algun carlos
![Pasted_image_20250901203416.png](Imagenes/Pasted_image_20250901203416.png)
le damos aceptar
asi se veria
![Pasted_image_20250901203610.png](Imagenes/Pasted_image_20250901203610.png)
ahora si recargamos el login vemos que somos carlos ya seria cuestion de eliminar el usuario
![Pasted_image_20250901203643.png](Imagenes/Pasted_image_20250901203643.png)
y logramos avanzar
![Pasted_image_20250901203703.png](Imagenes/Pasted_image_20250901203703.png)

