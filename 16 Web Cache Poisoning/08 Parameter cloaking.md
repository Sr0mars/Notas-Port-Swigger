En este laboratorio se explora la técnica de parameter cloaking, una forma avanzada de web cache poisoning que aprovecha que la caché ignora ciertos parámetros mientras que el back-end sí los interpreta. Aquí, el parámetro ‘**utm_content**‘ es ignorado por la caché, pero no por el servidor, lo que permite camuflar un segundo parámetro (**callback**) tras un punto y coma para alterar la lógica sin que se vea afectada la clave de caché.

La aplicación carga un script que ejecuta una función definida por el parámetro callback. Aunque este parámetro sí forma parte de la clave de caché cuando se incluye directamente, al camuflarlo dentro de ‘**utm_content**‘, es procesado por el servidor pero no considerado por la caché. Esto permite envenenar el recurso compartido con una llamada a ‘**alert(1)**‘, que se ejecutará cada vez que un usuario cargue ese archivo JavaScript en su navegador. La clave está en mantener la caché envenenada hasta que el usuario víctima acceda.

Solucion
interceptamos el home y podemos ver que tiene algo en la cookie vamos a buscar en el historico
![[Pasted image 20250821220459.png]]
y bueno esto lo mandamos al repeater
![[Pasted image 20250821220830.png]]
resumiendo un poco pues realmente no es de mucha importancia a pesar que se dirige hacia esto no se puede hacer mucho por que la ruta no se puede modificar por lo cual es algo dificil de vulnerar pero sin embargo se puede agregar parametros que ignorar el servidor como puede ser el utm (&utm_content=foo;callback=alert(1))
![[Pasted image 20250821221110.png]]de esta manera lo modificamos le damos a send
![[Pasted image 20250821221636.png]]
y miramos la alerta
![[Pasted image 20250821221619.png]]