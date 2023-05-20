# Создайте приложение для приготовления пасты. Приложение должно уметь создавать минимум три вида пасты. Классы
# различной пасты должны иметь следующие методы:
# Тип пасты;
# Соус;
# Начинка;
# Добавки.
# Для реализации используйте порождающие паттерны

class Pasta:
    def __init__(self):
        self._type = None
        self._sauce = None
        self._filling = None
        self._additives = None

    def __str__(self):
        return f'{self._type} pasta with {self._sauce} sauce, {self._filling} filling and {self._additives}'


class PastaBuilder:
    def __init__(self):
        self.pasta = Pasta()

    def build_pasta(self):
        self.build_type()
        self.build_sauce()
        self.build_filling()
        self.build_additives()

    def get_pasta(self):
        return self.pasta

    def build_type(self):
        pass

    def build_sauce(self):
        pass

    def build_filling(self):
        pass

    def build_additives(self):
        pass


class SpaghettiBologneseBuilder(PastaBuilder):
    def build_type(self):
        self.pasta._type = 'Spaghetti Bolognese'

    def build_sauce(self):
        self.pasta._sauce = 'Tomato'

    def build_filling(self):
        self.pasta._filling = 'Beef Bolognese'

    def build_additives(self):
        self.pasta._additives = 'Parmesan Cheese'


class SpaghettiCarbonaraBuilder(PastaBuilder):
    def build_type(self):
        self.pasta._type = 'Spaghetti Carbonara'

    def build_sauce(self):
        self.pasta._sauce = 'Carbonara'

    def build_filling(self):
        self.pasta._filling = 'Pancetta'

    def build_additives(self):
        self.pasta._additives = 'Cracked Black Pepper'


class AgnolottiPastaBuilder(PastaBuilder):
    def build_type(self):
        self.pasta._type = 'Piedmont'

    def build_sauce(self):
        self.pasta._sauce = 'Tomato or cream'

    def build_filling(self):
        self.pasta._filling = 'Beef'

    def build_additives(self):
        self.pasta._additives = 'Agnolotti al brazato'


class SpaghettiBologneseBuilder(PastaBuilder):
    def build_type(self):
        self.pasta._type = 'Spaghetti Bolognese'

    def build_sauce(self):
        self.pasta._sauce = 'Tomato'

    def build_filling(self):
        self.pasta._filling = 'Beef Bolognese'

    def build_additives(self):
        self.pasta._additives = 'Parmesan Cheese'


class PastaCreator:
    @staticmethod
    def make_pasta(builder):
        builder.build_pasta()
        return builder.get_pasta()


spaghetti_carbonara = PastaCreator.make_pasta(SpaghettiCarbonaraBuilder())
print(spaghetti_carbonara)
pasta_agnolotti = PastaCreator.make_pasta( AgnolottiPastaBuilder())
print(pasta_agnolotti)
spaghetti_bolognese = PastaCreator.make_pasta(SpaghettiBologneseBuilder())
print(spaghetti_bolognese)
