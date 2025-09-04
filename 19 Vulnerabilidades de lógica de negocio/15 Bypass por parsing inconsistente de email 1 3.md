En esta clase identificamos que el sistema restringe los registros únicamente a dominios **@ginandjuice.shop**. Comenzamos a probar codificaciones como **Q-encoding** en **iso-8859-1** y **UTF-8**, las cuales son correctamente detectadas como maliciosas.

Sin embargo, observamos que **UTF-7** no es bloqueado, lo que nos indica que podría haber una inconsistencia en la forma en que el servidor interpreta la dirección de correo.

Solucion
Importante Leer este post (https://portswigger.net/research/splitting-the-email-atom)
empezamos entrando a la web y registrandonos
![Pasted_image_20250829020059.png](/Imagenes/Pasted_image_20250829020059.png)
pero vemos que tiene una limitante la cual nos pide que si no tenemos ese correo no nos podemos registrar
