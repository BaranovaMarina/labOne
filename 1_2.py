def main():
    # Змінна для накопичення суми
    total_sum = 0

    # Цикл для перебору чисел у діапазоні від 500 до 1000
    for number in range(500, 1001):
        if number % 5 == 0:  # Перевірка кратності 5
            total_sum += number

    # Виведення результату
    print(f"Сума чисел, кратних 5, у діапазоні від 500 до 1000: {total_sum}")

# Запуск програми
main()
