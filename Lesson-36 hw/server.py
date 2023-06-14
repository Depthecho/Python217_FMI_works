import socket
import json
import threading
import requests

API_KEY = '67e9f11639ccecf9a690734c15f7aeb5'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
port = 12345

server_socket.bind((host, port))
print(f'Сервер запущен по адресу {host}, порту {port}')

server_socket.listen(5)


def handle_client(client_socket, client_address):
    print(f'Подключился клиент: {client_address}')
    message = 'Добро пожаловать! Вы подключены к серверу с погодой! '
    client_socket.send(message.encode())

    while True:
        client_message = client_socket.recv(1024).decode()

        if not client_message:
            print(f'Клиент {client_address} отключился')
            break

        words = client_message.split(',')
        words = list(map(str.strip, words))
        city, country = words[0], words[1]
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&units=metric&appid={API_KEY}'
        response = requests.get(url).json()
        if response['cod'] == 200:
            temperature = response['main']['temp']
            description = response['weather'][0]['description']
            response_text = f'Температура в {city}, {country} составляет {temperature}°C. Погода: {description}'
        else:
            response_text = 'Такой город и страна не найдены.'

        client_socket.send(response_text.encode())

    client_socket.close()


while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()