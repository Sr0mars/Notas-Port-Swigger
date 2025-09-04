En esta clase analizamos cómo una cookie de error (notification) permite recuperar datos desencriptados del servidor. Usamos esta funcionalidad como un oracle de desencriptación, descifrando nuestra propia cookie ‘**stay-logged-in**‘ para aprender su estructura: ‘**usuario:timestamp**‘. Este paso es esencial para falsificar una cookie válida como administrador.

Solucion
nos logeamos nos sale un casilla de stay login in le picamos y en el historico se refleja esto
![Pasted_image_20250829010441.png](/Imagenes/Pasted_image_20250829010441.png)
aqui tenemos un contenido en base64 vamos a decodificarlo pero no se puede leer
![Pasted_image_20250829010605.png](/Imagenes/Pasted_image_20250829010605.png)
y bueno investigando en la pagina concretamente en los post vamos a tratar de generar un error aproposito
![Pasted_image_20250829011035.png](/Imagenes/Pasted_image_20250829011035.png)
nos sale esto
![Pasted_image_20250829011058.png](/Imagenes/Pasted_image_20250829011058.png)
la cual la solicitud la vamos a mandar al repeater
![Pasted_image_20250829011213.png](/Imagenes/Pasted_image_20250829011213.png)
y vemos que en la respuesta tenemos un set cookie notification con una cadena en base64 que no es legible
![Pasted_image_20250829011439.png](/Imagenes/Pasted_image_20250829011439.png)
y si inspeccionamos en la web podemos ver que en el almacenamiento se translada otra coockie que pasa si la sustituimos
![Pasted_image_20250829011726.png](/Imagenes/Pasted_image_20250829011726.png)
![Pasted_image_20250829011858.png](/Imagenes/Pasted_image_20250829011858.png)
nos sale esto
![Pasted_image_20250829012012.png](/Imagenes/Pasted_image_20250829012012.png)
ahora nosotros podemos modificar esto salvo quitamos en el repeater el test y ponemos lo siguiente
![Pasted_image_20250829013010.png](/Imagenes/Pasted_image_20250829013010.png)
vemos en la resouesta que el valor de la cookie a aumentado
![Pasted_image_20250829013125.png](/Imagenes/Pasted_image_20250829013125.png)
y vamos a sustituirlo en la cookie y nos sale un nuevo error
![Pasted_image_20250829013237.png](/Imagenes/Pasted_image_20250829013237.png)el cual si vemos cuanto tiene 
![Pasted_image_20250829013426.png](/Imagenes/Pasted_image_20250829013426.png)
23 caracteres que tendremos que eliminar