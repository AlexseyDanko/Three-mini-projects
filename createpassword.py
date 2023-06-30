import random
import string

def generate_password(length=8):
    # Генерация пароля случайными символами
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        try:
            password_length = int(input("Введите длину пароля (0 для выхода): "))

            # Проверка на выход из программы
            if password_length == 0:
                break

            if password_length < 0:
                print("Длина пароля должна быть положительным числом.")
            else:
                password = generate_password(password_length)
                print("Сгенерированный пароль:", password)

        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")


if __name__ == '__main__':
    main()
