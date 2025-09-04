En esta clase trabajamos con una aplicación construida en Node.js y Express vulnerable a server-side prototype pollution. Observamos que al enviar datos como JSON en una funcionalidad legítima (cambio de dirección), el servidor los fusiona sin precaución con un objeto interno.

Aprovechamos esto inyectando un campo ‘**proto**‘ con una propiedad arbitraria, lo que modifica el prototipo global. Confirmamos que el servidor ha heredado esa propiedad observando la respuesta. Luego identificamos un gadget: la propiedad ‘**isAdmin**‘. Al establecerla en true dentro de ‘**proto**‘, escalamos privilegios y accedemos al panel de administración.

Esta clase demuestra cómo una simple entrada maliciosa en una petición JSON puede comprometer todo el control de acceso de una aplicación mal diseñada.

Solucion
en esta ocacion nos piden que nos logemos vemos que tiene lo interceptamos justo en el boton y mandamos al repeater
![Pasted_image_20250901000540.png](/Imagenes/Pasted_image_20250901000540.png)
vemos que en uno de los datos tenemos un false lo cual no me permite ser admin
![Pasted_image_20250901000758.png](/Imagenes/Pasted_image_20250901000758.png)
y mismo aqui podemos crear un prototipo para que se incluya de esta manera
"__proto__": {
    "foo":"bar"
}
Importante agregar la coma
![Pasted_image_20250901001539.png](/Imagenes/Pasted_image_20250901001539.png)
de esta manera obtenemos una nueva propiedad
entonces la idea es alterar el orden de las variables locales que contiene por lo cual admin lo convertimos a true de esta manera
"__proto__":{"isAdmin":"true"}
![Pasted_image_20250901001724.png](/Imagenes/Pasted_image_20250901001724.png)
y ya solo recargamos la pagina y eliminos al usuario carlos
![Pasted_image_20250901001840.png](/Imagenes/Pasted_image_20250901001840.png)

