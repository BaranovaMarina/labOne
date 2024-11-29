def print_pattern(n):
    """Функція для створення вказаного малюнка з віддзеркаленням"""
    # Перша частина (спадаючі рядки)
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    # Друга частина (зростаючі рядки)
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def main():
    """Основна функція програми"""
    try:
        n = int(input("Введіть ціле число N (2 ≤ N < 9): "))
        if 2 <= n < 9:
            print_pattern(n)
        else:
            print("Число має бути у межах від 2 до 8.")
    except ValueError:
        print("Помилка: введіть ціле число.")

# Запуск програми
main()
