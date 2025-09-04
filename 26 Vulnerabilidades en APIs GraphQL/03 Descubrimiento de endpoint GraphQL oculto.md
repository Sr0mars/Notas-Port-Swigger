En esta clase identificamos un endpoint GraphQL que no es accesible navegando por la interfaz del sitio. Enviamos peticiones GET a rutas comunes y detectamos una pista en la respuesta del endpoint ‘**/api**‘. Probamos una consulta universal que confirma que estamos ante un endpoint GraphQL activo.

Aunque la introspección está inicialmente bloqueada, conseguimos eludirla añadiendo un salto de línea que rompe la detección por expresión regular. Esto nos permite obtener el esquema completo. Desde ahí localizamos las consultas ‘**getUser**‘ y ‘**deleteOrganizationUser**‘, y al probar distintos IDs encontramos al usuario ‘**carlos**‘. Finalmente, enviamos una mutación para eliminarlo.

Esta clase demuestra cómo incluso endpoints GraphQL bien ocultos y protegidos pueden ser descubiertos y explotados con técnicas de evasión y análisis estructurado.

Solucion
empezamos navegando pero curiosamente no encontramos ningun graphql en el historico
![Pasted_image_20250901020442.png](Imagenes/Pasted_image_20250901020442.png)pero existen algunos endpoints
![Pasted_image_20250901020545.png](Imagenes/Pasted_image_20250901020545.png)
![Pasted_image_20250901020624.png](Imagenes/Pasted_image_20250901020624.png)
entre ellas esta la de api la ponemos en la url y nos dice que query no presente
![Pasted_image_20250901020656.png](Imagenes/Pasted_image_20250901020656.png)
si tratamos de ver que tipo de query es
![Pasted_image_20250901020830.png](Imagenes/Pasted_image_20250901020830.png)
no nos da mucha info pero de igual forma nos puede servir para ser una itroinspeccion lo mandamos al repeater
![Pasted_image_20250901020953.png](Imagenes/Pasted_image_20250901020953.png)
y bueno nos sale esto si lo seleccionamos podemos ver que se interpretar como una query
![Pasted_image_20250901021225.png](Imagenes/Pasted_image_20250901021225.png)
y lo que podemos hacer justo despues de donde dice __schema podemos darle un salto de linea con %0a
![Pasted_image_20250901021437.png](Imagenes/Pasted_image_20250901021437.png)
y esto sigue siendo valido y si le damos send
y vemos que es correcto asi que volvemos a mandarlo al site map
![Pasted_image_20250901021544.png](Imagenes/Pasted_image_20250901021544.png)
vemos 2 querys la primera se emplea un delete organization y el de abajo el getUser los 2 los mandamos al repeater
![Pasted_image_20250901021703.png](Imagenes/Pasted_image_20250901021703.png)
entonces que es lo que hace la peticion getUser busca el usuario
![Pasted_image_20250901021937.png](Imagenes/Pasted_image_20250901021937.png)
y el otro lo elimina
![Pasted_image_20250901022007.png](Imagenes/Pasted_image_20250901022007.png)
de esta manera nos regresamos ala pagina y hemos resuelto el lab
![Pasted_image_20250901022057.png](Imagenes/Pasted_image_20250901022057.png)

