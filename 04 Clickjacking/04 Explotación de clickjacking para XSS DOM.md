En este laboratorio se combina una vulnerabilidad de clickjacking con una XSS basada en DOM que se activa mediante un clic. El objetivo es engañar a la víctima para que pulse un botón en una página aparentemente inocente, lo que desencadena la ejecución de la función print() desde un payload XSS.

Para lograrlo, se incrusta la URL del formulario de feedback en un iframe, manipulando los parámetros de la URL para incluir un payload malicioso en el campo name. Este payload se aprovecha de una mala gestión de datos en el DOM, concretamente en la parte de la página que muestra los resultados del envío (#feedbackResult).

Mediante el uso de estilos CSS, se superpone un botón señuelo encima del botón real de “Submit feedback”. Gracias a la opacidad casi nula del iframe, la víctima no ve el contenido real del sitio y cree estar interactuando con la interfaz legítima.

Cuando la víctima hace clic en el botón señuelo, en realidad está interactuando con el botón del iframe, lo que activa el XSS basado en DOM y ejecuta print(), demostrando el ataque. La clave está en la precisión del alineamiento y en cómo se abusa del comportamiento inseguro del sitio en el manejo de parámetros reflejados en el DOM.

Solucion
Este es un laboratorio que es vulnerable a xss en la parte de la seccion de comentarios
![Pasted_image_20250724234055.png](Imagenes/Pasted_image_20250724234055.png)
![Pasted_image_20250724234107.png](Imagenes/Pasted_image_20250724234107.png)
una vez localizado la vulnerabilidad pues vamos a disfrazar el boton en esta ocacion pero poniendo los campos que tenemos en el formulario
<style>
	iframe {
        position:relative;
        width: 500px;
        height: 1000px;
        opacity: 0.0001;
    }
    div {
        position:absolute;
        top: 800px;
        left: 100px;
    }
</style>
<div>Click me</div>
<iframe
src="https://0a08007d0492094f80d66c3e00dd006d.web-security-academy.net/feedback?name=<img src=1 onerror=print()>&email=hacker@attacker-website.com&subject=test&message=test#feedbackResult"></iframe>

