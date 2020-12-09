"""
|------------------------------------|
|              Banners               |
|------------------------------------|
"""

def Get_Banner(target, port:int):

    try: 
        import socket
        
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Creamos el objeto socket

        sock.connect((target, port))  # Intentamos conectar con el objetivo en el puerto indicado

        sock.settimeout(2)

        targetBytes = target.encode()

        http_get = b'GET /index.html HTTP/1.1\r\nHost: ' + targetBytes + b'\r\nAccept: */*\r\n\r\n'

        data = ''

        sock.sendall(http_get)

        data = sock.recvfrom(1024)

        with open('Server_Banner.txt','w') as file:
            file.write(data[0].decode())

        print('Closing Connection!')

        sock.close()

    except:
        raise
