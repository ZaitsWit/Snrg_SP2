import math


def calculate_factorial(n):
    return math.factorial(n)


def main():
    print("Программа для вычисления факториала числа.")
    try:
        user_input = input("Введите положительное целое число: ")
        number = int(user_input)
        if number < 0:
            print("Ошибка: Введено отрицательное число. Пожалуйста, введите положительное целое число.")
        else:
            factorial_result = calculate_factorial(number)
            print(f"Факториал числа {number} равен: {factorial_result}")

    except ValueError:
        print("Ошибка: Введено не числовое значение. Пожалуйста, введите целое число.")


if __name__ == "__main__":
    main()