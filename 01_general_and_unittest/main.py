def validate_number(number):
    assert isinstance(number, int), "Потрібно ввести ціле число"
    if number <= 0:
        raise ValueError("Число повинно бути більшим за 0")
    return number
try:
    number = int(input("Введіть число: "))
    print("Результат:", validate_number(number))
except ValueError as error:
    print("Помилка:", error)
except AssertionError as error:
    print("Помилка:", error)
