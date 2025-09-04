# 1 Задание

try:

    a = float(input("Введите длину прямоугольника: "))
    b = float(input("Введите ширину прямоугольника: "))

    ploshchad = a * b
    perimetr = 2 * (a + b)

    print(f"Площадь прямоугольника: {ploshchad:.2f}")
    print(f"Периметр прямоугольника: {perimetr:.2f}")

except ValueError:
    print("Ошибка: Введите корректные числовые значения для сторон.")

# 2 Задание

try:
    num = int(input("Введите пятизначное целое число: "))

    if not (10000 <= num <= 99999):
        print("Ошибка: Число должно быть пятизначным (от 10000 до 99999).")
        exit()

    edinitsy = num % 10  # Единицы
    desyatki = (num // 10) % 10  # Десятки
    sotni = (num // 100) % 10  # Сотни
    tysyachi = (num // 1000) % 10  # Тысячи
    desyatki_tysyach = num // 10000  # Десятки тысяч

    stepen = desyatki ** edinitsy  # Десятки в степени единиц
    umnozh = stepen * sotni  # Умножение на сотни
    raznost = desyatki_tysyach - tysyachi  # Разность десятков тысяч и тысяч

    if raznost == 0:
        print("Ошибка: Разность десятков тысяч и тысяч равна нулю. Деление невозможно.")
        exit()

    result = umnozh / raznost
    print(f"Результат: {result}")

except ValueError:
    print("Ошибка: Введите корректное целое число.")