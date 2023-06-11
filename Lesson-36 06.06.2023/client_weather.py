import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
port = 12345

client_socket.connect((host, port))

server_message = client_socket.recv(1024).decode()
print(server_message)

while True:
    client_message = input('Введите сообщение: ')
    client_socket.send(client_message.encode())

    if not client_socket:
        print('Отключение...')
        break

    server_response = client_socket.recv(1024).decode()
    print(f'Ответ сервера: {server_response}')

client_socket.close()