En esta clase analizamos cómo, al comparar las peticiones GET y POST del endpoint de checkout, podemos descubrir un parámetro oculto llamado ‘**chosen_discount**‘.

Aprovechando la falta de validación, añadimos este parámetro manualmente al cuerpo de la solicitud POST y modificamos el valor del porcentaje de descuento a 100, logrando así comprar el artículo sin coste y resolviendo el laboratorio.

Solucion
nos logeamos
![Pasted_image_20250902030727.png](Imagenes/Pasted_image_20250902030727.png)
y intentamos comprar la chaqueta
![Pasted_image_20250902030806.png](Imagenes/Pasted_image_20250902030806.png)
y bueno si miramos en el historico podemos ver una peticion get y post hacia api esto lo mandamos al repeater
![Pasted_image_20250902030857.png](Imagenes/Pasted_image_20250902030857.png)
![Pasted_image_20250902031018.png](Imagenes/Pasted_image_20250902031018.png)
![Pasted_image_20250902031052.png](Imagenes/Pasted_image_20250902031052.png)
vemos que la tab 1 tiene el mismo formato que la tab2
vamos a copiar la cabecera que esta en la tab1 y la ponemos en la tab2
![Pasted_image_20250902031412.png](Imagenes/Pasted_image_20250902031412.png)
tal que no nos da ningun error vemos que se esta presenta un porcentaje de descuento vamos a meterle el 100
![Pasted_image_20250902031530.png](Imagenes/Pasted_image_20250902031530.png)
y si recargamos la pagina veremos que se a resuelto el lab
![Pasted_image_20250902031606.png](Imagenes/Pasted_image_20250902031606.png)
