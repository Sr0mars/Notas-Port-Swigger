Este laboratorio utiliza archivos de traducción basados en JSON para cambiar la interfaz según el idioma del usuario. Al inyectar una cabecera ‘**X-Forwarded-Host**‘ manipulada, se puede forzar al navegador a cargar un archivo JSON malicioso desde nuestro exploit server. Este archivo contiene traducciones alteradas para el idioma español, una de las cuales incluye un ‘**alert(document.cookie)**‘.

Aunque la víctima utiliza el idioma inglés, esta primera parte del ataque permite validar que es posible introducir un payload XSS en la versión en español. Se guarda el archivo en el exploit server y se confirma que la respuesta es cacheable incluyendo un parámetro de cache buster y observando el encabezado ‘**X-Cache: hit**‘.

Solucion
De primeras vamos a interceptar con bs lel flujo de la pagina
![Pasted_image_20250822183412.png](/Imagenes/Pasted_image_20250822183412.png)
podemos ver que se hacen varias peticiones
![Pasted_image_20250822183634.png](/Imagenes/Pasted_image_20250822183634.png)
vamos a intertar cambiar de idioma al español para ver que peticion nos da
![Pasted_image_20250822183741.png](/Imagenes/Pasted_image_20250822183741.png)
vemos que en la propia web tenemos un localized que puede ir aumentando
nos vamos al BS y podemos ver que se hace una peticion a setlang
![Pasted_image_20250822184106.png](/Imagenes/Pasted_image_20250822184106.png)
que si ponemos antencion se esta enviando hacia localized
entonces ya analizando un poco si nosotro por medio de la cache podemos envenear el boton de ver detalles con el exploit server es posible que nosotros podamos tener el control
![Pasted_image_20250822184303.png](/Imagenes/Pasted_image_20250822184303.png)
asi que esto lo vamos a mandar al repeater
de igual forma se visualizamos el pagina principal podemos ver como en laboratorios anteriores vemos que se aplica una data
![Pasted_image_20250822184855.png](/Imagenes/Pasted_image_20250822184855.png)
si filtramos podemos ver que tiene una variable
![Pasted_image_20250822185019.png](/Imagenes/Pasted_image_20250822185019.png)
la cual su buscamos en el historico se aplica aqui la cual nos lleva a una url de tipo json
![Pasted_image_20250822185128.png](/Imagenes/Pasted_image_20250822185128.png)
