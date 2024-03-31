import socket
import threading
from tqdm import tqdm

host = "localhost"

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((host, port))
        print(f"\nПорт {port} открыт")
        s.close()
    except:
        pass

threads = []
for port in tqdm(range(1, 10000), desc="Сканирование портов"):  # Сканирование портов с 1 по 10000
    thread = threading.Thread(target=scan_port, args=(host, port))
    threads.append(thread)
    thread.start()
