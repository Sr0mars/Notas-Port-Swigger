En esta clase analizamos cómo un simple comentario HTML puede exponer una ruta interna a una página de depuración (**/cgi-bin/phpinfo.php**). Al acceder a ella, obtenemos información sensible del entorno de la aplicación, como la variable **SECRET_KEY**, que utilizamos para completar satisfactoriamente el laboratorio.

Solucion
la web:
![Pasted_image_20250827221909.png](/Imagenes/Pasted_image_20250827221909.png)
si nosotros por medio de BS checamos podemos ver las rutas que contempla
![Pasted_image_20250827221942.png](/Imagenes/Pasted_image_20250827221942.png)
que de igual forma lo hubieramos encontrado si le ubieramos dado Ctrl+U
![Pasted_image_20250827222045.png](/Imagenes/Pasted_image_20250827222045.png)
![Pasted_image_20250827222109.png](/Imagenes/Pasted_image_20250827222109.png)
ya solo nos copiamos la secret key
![Pasted_image_20250827222216.png](/Imagenes/Pasted_image_20250827222216.png)y la ponemos en la web
![Pasted_image_20250827222252.png](/Imagenes/Pasted_image_20250827222252.png)
