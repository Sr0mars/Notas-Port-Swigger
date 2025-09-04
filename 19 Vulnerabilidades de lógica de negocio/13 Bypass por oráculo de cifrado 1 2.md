En esta clase analizamos cómo una cookie de error (notification) permite recuperar datos desencriptados del servidor. Usamos esta funcionalidad como un oracle de desencriptación, descifrando nuestra propia cookie ‘**stay-logged-in**‘ para aprender su estructura: ‘**usuario:timestamp**‘. Este paso es esencial para falsificar una cookie válida como administrador.

Solucion
nos logeamos nos sale un casilla de stay login in le picamos y en el historico se refleja esto
![Pasted image 20250829010441.png](imagenes/Pasted image 20250829010441.png)
aqui tenemos un contenido en base64 vamos a decodificarlo pero no se puede leer
![Pasted image 20250829010605.png](imagenes/Pasted image 20250829010605.png)
y bueno investigando en la pagina concretamente en los post vamos a tratar de generar un error aproposito
![Pasted image 20250829011035.png](imagenes/Pasted image 20250829011035.png)
nos sale esto
![Pasted image 20250829011058.png](imagenes/Pasted image 20250829011058.png)
la cual la solicitud la vamos a mandar al repeater
![Pasted image 20250829011213.png](imagenes/Pasted image 20250829011213.png)
y vemos que en la respuesta tenemos un set cookie notification con una cadena en base64 que no es legible
![Pasted image 20250829011439.png](imagenes/Pasted image 20250829011439.png)
y si inspeccionamos en la web podemos ver que en el almacenamiento se translada otra coockie que pasa si la sustituimos
![Pasted image 20250829011726.png](imagenes/Pasted image 20250829011726.png)
![Pasted image 20250829011858.png](imagenes/Pasted image 20250829011858.png)
nos sale esto
![Pasted image 20250829012012.png](imagenes/Pasted image 20250829012012.png)
ahora nosotros podemos modificar esto salvo quitamos en el repeater el test y ponemos lo siguiente
![Pasted image 20250829013010.png](imagenes/Pasted image 20250829013010.png)
vemos en la resouesta que el valor de la cookie a aumentado
![Pasted image 20250829013125.png](imagenes/Pasted image 20250829013125.png)
y vamos a sustituirlo en la cookie y nos sale un nuevo error
![Pasted image 20250829013237.png](imagenes/Pasted image 20250829013237.png)el cual si vemos cuanto tiene 
![Pasted image 20250829013426.png](imagenes/Pasted image 20250829013426.png)
23 caracteres que tendremos que eliminar