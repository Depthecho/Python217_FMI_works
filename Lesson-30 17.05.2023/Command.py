# Шаблон Command — это поведенческий шаблон
# проектирования, в котором существует абстракция
# между объектом, который вызывает команду, и
# объектом, который ее выполняет.

# Например, кнопка вызовет Invoker, который
# вызовет предварительно зарегистрированный Command,
# который выполнит Receiver.

from abc import ABC, abstractmethod

# Абстрактный класс для создания команд
class Command(ABC):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def process(self):
        pass

# Конкретная реализация команды
class CommandImplementation(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def process(self):
        self.receiver.perform_action()

# Объект-получатель
class Receiver:
    def perform_action(self):
        print('Action performed in receiver.')

# Объект вызывающий
class Invoker:
    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.process()


receiver = Receiver()
cmd = CommandImplementation(receiver)
invoker = Invoker()
invoker.command(cmd)  # Наша регистрируемая прослойка - команда
invoker.execute()

