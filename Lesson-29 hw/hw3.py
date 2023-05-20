# Создайте реализацию паттерна Prototype. Протестируйте работу созданного класса.


class MobileApp:
    def __init__(self, name, platform, price, description):
        self.name = name
        self.platform = platform
        self.price = price
        self.description = description

    def clone(self):
        return MobileApp(self.name, self.platform, self.price, self.description)


app1 = MobileApp("MyApp", "IOS", "Free on early acces", "App at the testing stage")
print(f"App: '{app1.name}'\n"
      f"Platform: {app1.platform}\n"
      f"Price: {app1.price}\n"
      f"{app1.description}")

print("==================================================================")

app2 = app1.clone()
app2.platform = "IOS and Android"
app2.price = "3.99$"
app2.description = "The application is completely ready and available for download !"
print(f"Clone app '{app2.name}'\n"
      f"Platform: {app2.platform}\n"
      f"Price: {app2.price}\n"
      f"{app2.description}")
