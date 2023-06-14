import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
port = 12345

client_socket.connect((host, port))

while True:
    message = input('Введите запрос в виде "city, country": ')
    client_socket.send(message.encode())

    if not client_socket:
        print('Отключение...')
        break

    response = client_socket.recv(1024).decode()
    print(f'Ответ сервера: {response}')

client_socket.close()

# Почему-то на первый инпут нет никакой реакции, когда ввожу город и страну, скрин приложу