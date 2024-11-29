def calculate_x(a, b):
    """Обчислення значення X за заданими умовами"""
    if a > b:
        return a * a - b
    elif a == b:
        return -a
    elif a < b:
        return (a * b - 1) / b

def main():
    """Основна функція програми"""
    try:
        # Введення значень a та b
        a = float(input("Введіть число a (від 1 до 100): "))
        b = float(input("Введіть число b (від 1 до 100): "))

        # Перевірка, чи входять числа до діапазону [1, 100]
        if not (1 <= a <= 100 and 1 <= b <= 100):
            print("Помилка: числа a та b повинні бути в діапазоні від 1 до 100!")
            return

        # Обчислення X
        x = calculate_x(a, b)
        print(f"Результат: X = {x}")

    except ValueError:
        print("Помилка: введіть коректні числові значення!")
main()
