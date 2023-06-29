def check_password_strength(password):
    score = 0

    # Проверка длины пароля
    if len(password) < 8:
        return 0

    score += len(password) // 2

    # Проверка наличия цифр в пароле
    if any(char.isdigit() for char in password):
        score += 2

    # Проверка наличия букв в верхнем регистре и нижнем регистре в пароле
    if any(char.isupper() for char in password) and any(char.islower() for char in password):
        score += 3

    # Проверка наличия специальных символов в пароле
    if any(not char.isalnum() for char in password):
        score += 4

    # Ограничение максимального балла до 10
    if score > 10:
        score = 10

    return score


# Главная функция программы
def main():
    while True:
        password = input("Введите пароль: ")
        strength_score = check_password_strength(password)
        print("Баллы надежности пароля:", strength_score)

        choice = input("Хотите проверить еще один пароль? (y/n): ")
        if choice.lower() != "y":
            break


# Запуск программы
if __name__ == '__main__':
    main()
