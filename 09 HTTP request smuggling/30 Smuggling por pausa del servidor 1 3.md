En esta primera parte analizamos el comportamiento del servidor frente a redirecciones internas, lo que nos lleva a detectar un vector de desincronización basado en pausas.

Esta técnica nos permite confirmar que el servidor procesa dos peticiones en una sola conexión y revela que es vulnerable a desyncs tipo CL.0.

Solucion
/opt/BurpSuiteCommunity/BurpSuiteCommunity

Lo primero sera interceptar un endpoint de la pagina para esto nos vamos al http history e interceptamos el resources lo hacemos post
![[Pasted image 20250812230602.png]]
asi que vamos a empezar a probar cosas para ver si nos salen errores pero de igual forma vamos a interceptar una peticion hacia la raiz
la cual va ser nuestro normal request y lo hacemos http 1
![[Pasted image 20250812231308.png]]

