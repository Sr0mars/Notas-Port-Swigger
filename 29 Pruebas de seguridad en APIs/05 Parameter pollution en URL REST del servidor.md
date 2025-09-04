En esta clase analizamos cómo, inyectando secuencias como ‘**../**‘ dentro del parámetro **username**, podemos recorrer el árbol de rutas del servidor hasta localizar el archivo ‘**openapi.json**‘, el cual revela endpoints internos de la API. Utilizando esa información, logramos acceder al token de reseteo de contraseña del administrador modificando dinámicamente la ruta del endpoint a través del parámetro.

Finalmente, reseteamos la contraseña del administrador y accedemos a su cuenta para completar el laboratorio.

Solucion
no nos dan credenciales por lo tanto nos vamos a forgot
![Pasted_image_20250902031824.png](/Imagenes/Pasted_image_20250902031824.png)
ponemos al administrador
![Pasted_image_20250902031851.png](/Imagenes/Pasted_image_20250902031851.png)
nos sale esto
![Pasted_image_20250902031903.png](/Imagenes/Pasted_image_20250902031903.png)
si checamos el historico vemos que se ah empleado una solicitud get y post a forgot password esto lo mandamos al repeater
![Pasted_image_20250902032010.png](/Imagenes/Pasted_image_20250902032010.png)si no le gusta el # podemos probar otra cosa
![Pasted_image_20250902032154.png](/Imagenes/Pasted_image_20250902032154.png)
sin embargo si probamos con ./ como si fuera una ruta si le gusta
![Pasted_image_20250902032407.png](/Imagenes/Pasted_image_20250902032407.png)
entonces podemos probar un diccionario que contempla diccionarios paths api ([Common api paths.. swagger..openapi.. · GitHub](https://gist.github.com/rodnt/250dd33af97d228cc94cd11504abef06))
vamos a crear un diccionario con todo esas rutas para pasarlo al intruder
antes vamos a retroceder un par de directorios y vamos a pasarle el # %23
![Pasted_image_20250902032843.png](/Imagenes/Pasted_image_20250902032843.png)
![Pasted_image_20250902032924.png](/Imagenes/Pasted_image_20250902032924.png)
vamos a filtrar por longitud y vemos que nos regresa un api.json
![Pasted_image_20250902033109.png](/Imagenes/Pasted_image_20250902033109.png)
si checamos podemos ver en el response que hay varias rutas
de la cual destaca (/api/internal/v1/users/{username}/field/{field})
y algo que podemos probar es como nos esta dando el campo field probarlo en el response
![Pasted_image_20250902033440.png](/Imagenes/Pasted_image_20250902033440.png)
nos dice que nos pide forzosamente el campo email
![Pasted_image_20250902033515.png](/Imagenes/Pasted_image_20250902033515.png)
y este nos lo resuelve
asi que si vemos la otra tab nos sale una direccion
![Pasted_image_20250902033656.png](/Imagenes/Pasted_image_20250902033656.png)
y si la pegamos nos sale esto
![Pasted_image_20250902033730.png](/Imagenes/Pasted_image_20250902033730.png)
de igual forma nos pide forzosamente el campo email por que la version solo soporta eso
pero que pasa si retrocedesmo algunos directorios y ponesmo la version
![Pasted_image_20250902033932.png](/Imagenes/Pasted_image_20250902033932.png)
de tal manera que aqui si nos deja y nos da el token
y quedaria asi en la url
![Pasted_image_20250902034045.png](/Imagenes/Pasted_image_20250902034045.png)
asi que cambiamos la contraseña
![Pasted_image_20250902034121.png](/Imagenes/Pasted_image_20250902034121.png)
nos volvemos a logear pero en este caso como administrador y ya solo eliminamos al usuario carlos
![Pasted_image_20250902034159.png](/Imagenes/Pasted_image_20250902034159.png)



