import random


def generate_secret_number():
    # Функция генерирует четырёхзначное число, которое нужно угадать.
    digit = random.randint(1000, 9999)
    return str(digit)


def count_bulls_and_cows(secret: str, guess: str) -> tuple[int, int]:
    # Функция принимает секретное и предполагаемое число, и возвращает количество быков и коров.
    bulls = 0
    cows = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1
        elif secret[i] in guess:
            cows += 1
    return bulls, cows


def play_game(secret_number: str, attempts: int) -> int:
    # Функция рекурсивно запрашивает у пользователя предполагаемое число, пока не будет угадано.
    guess = input("Введите четырёхзначное число: ")
    if len(guess) != 4 or not guess.isdigit():
        print("Неверный ввод, попробуйте ещё раз")
        return play_game(secret_number, attempts)
    bulls, cows = count_bulls_and_cows(secret_number, guess)
    print(f"Быков: {bulls}, коров: {cows}")
    attempts += 1
    if bulls == 4:
        print(f"Вы угадали число {secret_number} за {attempts} попыток!")
        return
    return play_game(secret_number, attempts)


secret_number = generate_secret_number()
# print(secret_number) # Вывод заданного компьютером числа.
print("Добро пожаловать в игру \"Быки и коровы\"!")
play_game(secret_number, 0)


