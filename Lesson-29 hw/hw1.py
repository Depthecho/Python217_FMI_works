# Создайте реализацию паттерна Builder. Протестируйте работу созданного класса.

class MobileApp:
    def __init__(self):
        self.name = None
        self.platform = None
        self.price = None
        self.description = None

    def __str__(self):
        return f"App name: {self.name}\n"\
               f"Platform: {self.platform}\n"\
               f"Price: {self.price}\n"\
               f"Description: {self.description}"


class MobileAppBuilder:
    def __init__(self):
        self.app = MobileApp()

    def set_name(self, name):
        self.app.name = name
        return self

    def set_platform(self, platform):
        self.app.platform = platform
        return self

    def set_price(self, price):
        self.app.price = price
        return self

    def set_description(self, description):
        self.app.description = description
        return self

    def build(self):
        return self.app


app_builder = MobileAppBuilder().set_name("MyApp").set_platform("iOS").set_price("1.99$").set_description("Rly cool app"
                                                                                                          )
app = app_builder.build()
print(app)