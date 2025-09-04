En esta clase trabajamos con una vulnerabilidad de XSS basado en DOM que se dispara cuando el navegador detecta un cambio en la parte del hash de la URL —es decir, todo lo que viene después del símbolo de almohadilla.

La aplicación utiliza jQuery para seleccionar elementos basándose en ese valor y realizar acciones como hacer scroll automático a un post específico. El problema es que se emplea directamente como selector, sin validación alguna, permitiendo al atacante manipularlo para inyectar y ejecutar código en el navegador de la víctima.

Montamos un ataque usando un servidor de explotación que carga la página vulnerable dentro de un contenedor invisible. Al modificarse dinámicamente la URL interna, se inyecta una instrucción que se ejecuta automáticamente mediante un evento de error, invocando una función del navegador como demostración.

Esta clase muestra cómo incluso fragmentos aparentemente inofensivos de la URL, como el hash, pueden ser vectores de ataque si no se gestionan correctamente en el lado cliente.

Solucion 
Lo primero visualizar la pagina y ver el codigo fuente 
![Pasted image 20250705162445.png](imagenes/Pasted image 20250705162445.png)

Lo segundo identificar la parte del script y ver que hace
  $(window).on('hashchange', function(){
                            var post = $('section.blog-list h2:contains(' + decodeURIComponent(window.location.hash.slice(1)) + ')');
                            if (post) post.get(0).scrollIntoView();
                        });
![Pasted image 20250705162708.png](imagenes/Pasted image 20250705162708.png)
Entonces lo lo que podemos hacer es llamar por medio de # algun titulo por ejemplo despues que termina la url ponemos #scams
![Pasted image 20250705163348.png](imagenes/Pasted image 20250705163348.png)
lo que hace que al volver poner la consulta me salga como resultado scams 
entones con BS podemos interceptar el codigo esto en el apartado de script
![Pasted image 20250705163739.png](imagenes/Pasted image 20250705163739.png)
y lo podemos probar en la url
![Pasted image 20250705163946.png](imagenes/Pasted image 20250705163946.png)
entonces con esto nos podemos aprobechar de esto pero con la ayuda de un servidor malicioso modificando la url


