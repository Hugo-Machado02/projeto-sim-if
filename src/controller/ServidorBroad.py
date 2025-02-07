import socket
import time
import psutil

def obter_ip_local():
    """Retorna o IP da interface do Radmin VPN."""
    for interface, info in psutil.net_if_addrs().items():
        for endereco in info:
            if interface.startswith("Radmin"):  # Filtra pelo nome da interface
                if endereco.family == socket.AF_INET:  # Verifica se é IPv4
                    return endereco.address
    return None  # Retorna None se não encontrar

def broadcast_cidade():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    ip = obter_ip_local()
    mensagem = f"CIDADE:{ip}:5000"

    while True:
        sock.sendto(mensagem.encode(), ('255.255.255.255', 37020))
        print("Broadcast enviado:", mensagem)
        time.sleep(5)

broadcast_cidade()