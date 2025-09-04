En esta clase exploramos cómo una documentación de API mal protegida puede volverse un vector de ataque. Accedemos al endpoint **/api**, el cual revela una interfaz interactiva con operaciones disponibles. Desde esta documentación, descubrimos la posibilidad de eliminar usuarios, y aprovechamos esta funcionalidad para borrar al usuario carlos.

Esta técnica destaca la importancia de restringir el acceso a documentación sensible que podría revelar rutas críticas.

Solucion
![[Pasted image 20250902020922.png]]
La web:
![[Pasted image 20250902021103.png]]
nos logeamos ahora vamos a cambiar el correo
![[Pasted image 20250902021153.png]]
nos vamos al historico y vemos una seccion api un metodo patch y esto lo mandamos al repeater
![[Pasted image 20250902021243.png]]
![[Pasted image 20250902021357.png]]
vamos a empesar a eliminar directorios y en api nos sale 302
![[Pasted image 20250902021547.png]]
vamos a cambiar el metodo a get y eliminanos eso del email
![[Pasted image 20250902021646.png]]
esto lo vamos a poner en el navegador
![[Pasted image 20250902021734.png]]
![[Pasted image 20250902021759.png]]
y bueno estos metodos los ponemos en el BS de modo que como el objetivo es eliminar a carlos vamos usar el metofo DELETE
![[Pasted image 20250902022046.png]]
![[Pasted image 20250902022059.png]]



