import random
import constants


# Функция проверки правильности введенного числа
def is_valid_num(num):
    try:
        num = int(num)
        return num
    except ValueError:
        print("Введите корректное корректное число")
        num = input()
        num = is_valid_num(num)
        return num

# Функция проверки ответа пользователя о составе пароля
def is_valid_answer(ans, char):
    if ans == 'y' or ans == 'n':
        if ans == 'y':
            return True
        else:
            return False
    else:
        print("Введите корректный ответ Y или N:")
        ans = input()
        if is_valid_answer(ans, char):
            return True
        else:
            return False



# Функция определяющая количество паролей и их состав
def what_in_pass(quant):
    passwords = []
    symbols = [constants.digits, constants.lowercase_letters, constants.uppercase_letters, constants.punctuation]
    for i in range(1, quant + 1):
        # Переменная символов пароля
        chars = ""
        print("Какой длины должен быть", i, "пароль")
        length = input()
        length = is_valid_num(length)
        for k in range(len(symbols)):
            print("Должен ли пароль включать в себя:", symbols[k], "Y/N?")
            answer = input().lower()
            if is_valid_answer(answer, symbols[k]):
                chars += symbols[k]
        passwords.append(generate_password(chars, length))
    return passwords


# Функция генерации пароля
def generate_password(pass_chars, pass_length):
    password = ""
    l_chars = pass_chars.split()
    print(len(pass_chars))
    print(l_chars)
    for i in range(pass_length):
        password += l_chars[random.randint(0, len(pass_chars) - 1)]
    return password


# Главная программа
print("Добро пожаловать в генератор безопасных паролей!")
print("Укажите количество паролей, которые необходимо сгенерировать.")
quantity = input()
quantity = is_valid_num(quantity)
print(what_in_pass(quantity))


