En este laboratorio se utiliza la técnica de fat GET request, donde el cuerpo de una petición GET es procesado por el servidor pero ignorado por la caché. Esta diferencia permite modificar el comportamiento de un recurso compartido sin alterar su clave de caché.

El objetivo es manipular la función JavaScript **callback** utilizada en el script ‘**/js/geolocate.js**‘. Aunque la clave de caché se basa en el valor del parámetro en la URL, el servidor procesa también un valor duplicado del mismo parámetro enviado en el cuerpo de la petición. Al incluir ‘**alert(1)**‘ como valor del parámetro en el cuerpo, el script se modifica sin que la caché lo detecte, envenenando así la respuesta que recibirán los usuarios posteriores. La cache debe mantenerse activa hasta que el usuario víctima acceda, momento en el que se resolverá el laboratorio.

Solucion
interceptamos el home
de igual manera si nosotros vemos el el historico tenemos de nuevo la direccion de geolocate
![Pasted image 20250821222043.png](imagenes/Pasted image 20250821222043.png)
esto lo mandmaos al repeter y si usamos la cabecera callback por que el web cache lo ignora por locual nosotros la ponemos y mandamos un alert
![Pasted image 20250821222243.png](imagenes/Pasted image 20250821222243.png)
![Pasted image 20250821222254.png](imagenes/Pasted image 20250821222254.png)
