import socket

def escutar_broadcast():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind(('', 37020))

    print("Aguardando cidades...")
    while True:
        data, addr = sock.recvfrom(1024)
        print("Cidade descoberta:", data.decode(), "de", addr)

escutar_broadcast()