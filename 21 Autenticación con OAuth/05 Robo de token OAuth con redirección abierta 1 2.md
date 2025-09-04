En esta primera clase, se estudia cómo una mala validación del parámetro redirect_uri por parte del servidor OAuth permite concatenar rutas como ‘**/../**‘ al callback legítimo, logrando una redirección hacia otros puntos dentro del mismo dominio. Al completar el login con OAuth, se observa que el access_token queda incluido en el fragmento de la URL.

Posteriormente, se analiza el comportamiento de la funcionalidad “Siguiente post”, la cual redirige al usuario a la URL indicada en un parámetro **path**. Se demuestra que este componente es una redirección abierta (open redirect) que permite enviar al usuario a cualquier dominio externo.

El objetivo de esta clase es comprender cómo estas dos debilidades —una redirección relativa con traversal más una redirección abierta— pueden encadenarse para construir un ataque completo, preparando el terreno para la explotación que se realiza en la segunda clase.

Solucion
nos logeamos y la idea es encontrar un open redirect
en el historico vemos un call back
![Pasted_image_20250830012955.png](/Imagenes/Pasted_image_20250830012955.png)
la vamos a ver donde se aplica un redirect
investigando la pagina podemos ver que en uno de los post de aplica una ruta path
nos copiamos la url
![Pasted_image_20250830013114.png](/Imagenes/Pasted_image_20250830013114.png)
![Pasted_image_20250830013131.png](/Imagenes/Pasted_image_20250830013131.png)
la cual nos lleva a esto "https://0a350042031ba53980437b44003200f3.web-security-academy.net/post/next?path=/post?postId=10"
y aqui en esta parte el path me puede redirigir a otra ruta
nos vamos aquedar con esto
post/next?path=
asi que vamos a interceptar nuevamente la parte del login exactamente esto
![Pasted_image_20250830013714.png](/Imagenes/Pasted_image_20250830013714.png)
![Pasted_image_20250830013826.png](/Imagenes/Pasted_image_20250830013826.png)
y ahi es donde vamos a retroceder algunos directorios y vamos aponer el path
![Pasted_image_20250830014045.png](/Imagenes/Pasted_image_20250830014045.png)
y si lodamos unos forwads podemos ver que al final si nos redirige
![Pasted_image_20250830014126.png](/Imagenes/Pasted_image_20250830014126.png)
y vemos que en la misma url nos da info
![Pasted_image_20250830014207.png](/Imagenes/Pasted_image_20250830014207.png)
y si miramos el historico en una de las respuestas podemos ver que nos redirige
![Pasted_image_20250830014510.png](/Imagenes/Pasted_image_20250830014510.png)
con un callback que seria lo mismo que vemos en una de las peticiones de abajo
![Pasted_image_20250830014603.png](/Imagenes/Pasted_image_20250830014603.png)
asi que necesitamos un authorization valido en este caso podemos utilizar el del exploit server

