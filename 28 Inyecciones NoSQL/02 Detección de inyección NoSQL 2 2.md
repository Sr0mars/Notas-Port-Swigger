Aquí evaluamos cómo insertar condiciones booleanas dentro de una consulta MongoDB para alterar la respuesta de la aplicación. Comparamos el comportamiento de la aplicación cuando usamos expresiones que devuelven falso frente a expresiones verdaderas.

Al introducir condiciones como **‘ || 1 || ‘**, logramos que el sistema ignore los filtros iniciales y devuelva resultados normalmente ocultos.

Esta técnica nos permite confirmar de forma práctica una inyección NoSQL funcional.

Solucion
![[Pasted image 20250902002106.png]]
![[Pasted image 20250902002604.png]]
![[Pasted image 20250902002826.png]]

