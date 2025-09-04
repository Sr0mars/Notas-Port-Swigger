Identificamos el GUID del usuario carlos accediendo a una publicación suya y copiando su ID desde la URL.

Luego, modificamos el parámetro id en nuestra página de cuenta con ese identificador para obtener su API key, explotando así una escalada horizontal de privilegios basada en identificadores poco protegidos.

Solucion
aqui podemos ver que en este caso nos otrorga un id en la parte de la url
![Pasted_image_20250815181703.png](Imagenes/Pasted_image_20250815181703.png)
por lo cual necesitamos un id de usuario para poder entrar
pero checando en los post podemos ver que el usuario carlos en la url nos entrega un identificador
![Pasted_image_20250815181814.png](Imagenes/Pasted_image_20250815181814.png)
por lo cual su nosotros hacemos Ctrl+u y filtramos por userid, podemos ver el id de carlos
![Pasted_image_20250815181949.png](Imagenes/Pasted_image_20250815181949.png)
entonces si nosotro lo suplantamos ya somos el usuario carlos
![Pasted_image_20250815182125.png](Imagenes/Pasted_image_20250815182125.png)
