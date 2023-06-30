def generate_fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    while True:
        try:
            n = int(input("Введите количество элементов последовательности Фибоначчи (0 для выхода): "))

            # Проверка на выход из программы
            if n == 0:
                break

            if n < 0:
                print("Количество элементов должно быть положительным числом.")
            else:
                fibonacci_sequence = generate_fibonacci_sequence(n)
                print("Последовательность Фибоначчи:", fibonacci_sequence)

        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")


if __name__ == '__main__':
    main()
