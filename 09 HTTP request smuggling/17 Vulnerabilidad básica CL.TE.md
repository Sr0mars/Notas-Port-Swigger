En esta clase abordamos un ataque de HTTP request smuggling CL.TE en su forma más simple. Aprovechamos que el front-end no admite chunked encoding, pero el back-end sí, para inyectar un fragmento que hará que la siguiente petición se interprete con un método inválido como GPOST. Esto nos permite confirmar la vulnerabilidad observando la respuesta del servidor. Es un ejemplo práctico y directo para entender cómo los desajustes entre servidores pueden ser explotados.

Solucion
Vamos a interceptar el home y modificamos el payload
![[Pasted image 20250809232526.png]]
