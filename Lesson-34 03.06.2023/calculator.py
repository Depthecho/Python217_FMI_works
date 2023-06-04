class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        assert b != 0, "We cannot divide on 0"
        return a / b

    @staticmethod
    def maximum(a, b):
        return max(a, b)

    @staticmethod
    def minimum(a, b):
        return min(a, b)

    @staticmethod
    def percentage(a, b):
        return (a * b) / 100

    @staticmethod
    def power(a, b):
        return a ** b