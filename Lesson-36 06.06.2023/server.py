import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
port = 12345
server_socket.bind((host, port))


server_socket.listen(5)
print('Сервер запущен и ждёт подключения.')

while True:
    client_socket, client_address = server_socket.accept()
    print(f'Подключен клиент: {client_address}')

    welcome_message = 'Добро пожаловать ! Вы подключены к серверу для обмена сообщениями. Введите сообщение: '
    client_socket.send(welcome_message.encode())

    while True:
        client_message = client_socket.recv(1024).decode()
        if not client_message:
            print(f'Клиент отключился: {client_address}')
            break

        print(f'Сообщения от клиента {client_address}: {client_message}')

        server_response = input('Ответа сервера: ')
        if not server_response:
            server_response = 'Сервер разорвал соединение'
        client_socket.send(server_response.encode())

    client_socket.close()