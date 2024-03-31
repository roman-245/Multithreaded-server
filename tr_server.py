import socket
import threading

def client_handler(client_socket):
    request = client_socket.recv(1024)
    #print(f"Получено сообщение от клиента: {request.decode()}")
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 8888))  # Привязка к localhost и порту 8888
    server.listen(5)  # Ожидание подключения до 5 клиентов

    print("Сервер запущен. Ожидание подключений...")

    while True:
        client_socket, addr = server.accept()
        print(f"Установлено соединение с {addr[0]}:{addr[1]}")

        client_thread = threading.Thread(target=client_handler, args=(client_socket,))
        client_thread.start()

start_server()