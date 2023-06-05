class Number:
    def __init__(self, value):
        self.value = value

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    # Перевод числа в восьмеричную систему счисления:
    def to_octal(self):
        octal = ''

        while self.value > 0:
            octal = str(self.value % 8) + octal
            self.value //= 8

        return '0o' + octal

    # Перевод числа в шестнадцатеричную систему счисления:
    def to_hexadecimal(self):
        hex_chars = '0123456789ABCDEF'
        hexadecimal = ''

        while self.value > 0:
            remainder = self.value % 16
            hexadecimal = hex_chars[remainder] + hexadecimal
            self.value //= 16

        return '0x' + hexadecimal

    # Перевод числа в двоичную систему счисления:
    def to_binary(self):
        binary = ''

        while self.value > 0:
            binary = str(self.value % 2) + binary
            self.value //= 2

        return '0b' + binary