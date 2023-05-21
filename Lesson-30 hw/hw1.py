# Создайте реализацию паттерна Command. Протестируйте работу созданного класса

from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class OpenApp(Command):
    def execute(self):
        print("Открытие приложения...")


class CloseApp(Command):
    def execute(self):
        print("Закрытие приложения...")


class SendNotification(Command):
    def execute(self):
        print("Отправка уведомления...")


class MobileApp:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def run_commands(self):
        for command in self.commands:
            command.execute()


app = MobileApp()
app.add_command(OpenApp())
app.add_command(SendNotification())
app.add_command(CloseApp())
app.run_commands()