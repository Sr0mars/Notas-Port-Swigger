En esta última parte del laboratorio aprovechamos el gadget identificado para construir un exploit real. Utilizamos el servidor de explotación proporcionado por la plataforma para crear un script que redirige a la víctima a una URL con un fragmento especialmente diseñado, el cual introduce la propiedad ‘**hitCallback**‘ con un valor malicioso: ‘**alert(document.cookie)**‘.

Al cargar la página, el navegador ejecuta el código inyectado y revela las cookies del usuario. Esta clase demuestra cómo los vectores de prototype pollution pueden aprovecharse en entornos reales para llevar a cabo ataques de robo de información en el lado cliente, incluso a través de bibliotecas de terceros aparentemente confiables.

de modo que nuestro exploit server quedaria algo asi
![Pasted_image_20250901000125.png](Imagenes/Pasted_image_20250901000125.png)
y con esto lo resolvemos
![Pasted_image_20250901000201.png](Imagenes/Pasted_image_20250901000201.png)
